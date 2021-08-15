#! /usr/bin/python3

import os
import sys
import subprocess
import click
import logging
import re


class PID:
    def __init__(self,string):
        self.pid = str(string)
    def __repr__(self):    
        return str(self.pid)

def get_bin(h):
    ''' Capabilities Display Script '''
    b = bin(h)
    return '{:0>64}'.format(b[2:])

def get_capabilities_human(n):
  ''' Given capbility set bits n, return human readable form '''
  capabilities = []
  for i,j in enumerate(n):
    if int(j):
        k = capabilities_bit.get(str(63-i))
        if not k:
             k = j
        capabilities.append(k)
  return ",".join(capabilities)

capabilities_bit = {}

scraped_capabilities = subprocess.check_output('grep "#define CAP_" /usr/include/linux/capability.h', shell=True, text=True)

capabilities_lines = scraped_capabilities.split("\n") 

for line in capabilities_lines: 
    line= line.strip() 
    cap_human = line.split()[1] 
    cap_bit = line.split()[2] 
    if (cap_human == "CAP_LAST_CAP"): 
        break 
    capabilities_bit[cap_bit] = cap_human

def checkerr(err,message):
   ''' Error checker and formatter '''
   if err:
       needle = r".*/proc/(\d*)/status.*" 
       haystack = message
       m = re.match(needle,haystack)
       if m:
           wrong_pid = m[1]
           err_message = "PID {} does not exist!".format(wrong_pid)
       else:
           err_message = message

       logging.error("{}".format(err_message))
       sys.exit(1)

@click.command()
@click.option('--pid', type=PID, default=str(os.getpid()),
                help='Process or Task ID')
def cli(pid,):
    ''' Capabilities Display Script '''
    spid = str(pid)
    err,name_ppid = subprocess.getstatusoutput(f'grep -E "^Name|^Tgid|^P{{0,1}}Pid|^Uid|^Gid" /proc/{spid}/status')
    checkerr(err, name_ppid)
    click.echo("{}\n".format(name_ppid.strip()))


    err,cap_output = subprocess.getstatusoutput(f'grep "Cap" /proc/{spid}/status')
    checkerr(err, cap_output)
    cap_outputs = cap_output.strip().split("\n")

    cap_outputs_dict = {}

    for line in cap_outputs:
        line = line.strip()
        cap_set = line.split(":\t")[0]
        cap_in_hex = line.split(":\t")[1]
        cap_in_dec = int(cap_in_hex,16)
        cap_in_bin = get_bin(cap_in_dec)
        cap_human = get_capabilities_human(cap_in_bin).lower()
        if not cap_human:
            cap_human = "None"
        click.echo("{}:\t {} \t {}".format(cap_set,cap_in_hex,cap_human))

