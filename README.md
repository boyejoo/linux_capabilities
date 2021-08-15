# linux_capabilities
Scripts and codes for Linux Capabilities study

## cap_display.py
Simple app to display capability sets attached to a process in human readable form by scraping */proc/pid/status* and resolves hexadecimal representation of capabilities by scaping capabiltity bit numbers in */usr/include/linux/capability.h*. 

### Installation
#### Install virtual environment
1. install python3-venv

        sudo apt install python3-venv


2. In suitable directory clone repository

        git clone https://github.com/boyejoo/linux_capabilities.git
        cd linux_capabilities

3. Install and activate venv

        python3 -m venv .
        source bin/activate
        
4. Install dependencies and application

        pip install .       

### Usage

        Usage: cap_display [OPTIONS]

          Capabilities Display Script

        Options:
          --pid PID  Process or Task ID
          --help     Show this message and exit.

        

        
