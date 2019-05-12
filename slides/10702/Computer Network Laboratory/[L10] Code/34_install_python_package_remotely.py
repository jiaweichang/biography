#!/usr/bin/env python
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

from getpass import getpass
from fabric.api import settings, run, env, prompt


def remote_server():
    env.hosts = ['localhost']
    env.user = prompt('Enter user name: ')
    env.password = getpass('Enter password: ')
    
def install_package():
    run("pip install yolk")

if __name__ == '__main__':
    install_package()
