from setuptools import setup

setup(
        name='cap_display',
        version='1.0',
        py_modules=['cap_display'],
        install_requires=[
            'Click',
            ],
        entry_points='''
        [console_scripts]
        cap_display=cap_display:cli
        ''',
        )

