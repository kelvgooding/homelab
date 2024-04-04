"""
Author: Kelv Gooding
Created: 2024-02-03
Updated: 2024-04-04
Version: 1.2
Description: A python script to generate the inventory file for Ansible.
"""

# Modules

import socket
import os
from datetime import datetime
import shutil

# Variables

base_path = f'/home/{os.environ.get("USER")}/homelab/ansible/'
filename = 'inventory'
dt = datetime.today().strftime("%d%m%Y_%H%M%S")

# Arrays

hostname_vm = [
    'vm-snowmoon',
    'vm-core',
]

# Script

def generate_inventory(inventory_group, server_group):

    # If inventory file already exists, creating a copy named inventory_ddmmyyyy_hhmmss

    if os.path.isfile(os.path.join(base_path, filename)):
        print(f'{os.path.join(base_path, filename)} file already exists. {os.path.join(base_path, filename)} has been renamed to {os.path.join(base_path, filename)}_{dt}')
        shutil.copy(f'{os.path.join(base_path, filename)}', f'{os.path.join(base_path, filename)}_{dt}')

    # Creating inventory file

    with open(os.path.join(base_path, filename), 'a') as f:
        try:
            for hostname in server_group:

                # Check if IP can be obtained from hostname

                ip_address = socket.gethostbyname(hostname)

                # Write hostname and IP address to inventory file

                f.write(f'[{hostname}]\n')
                f.write(f'{ip_address}\n\n')

            # Create a group for the hosts

            f.write(f'[{inventory_group}:children]\n')
            for item in server_group:
                f.write(f'{item}\n')
            f.write('\n')

        # If IP address cannot be found from the hostname, continue to iterate

        except socket.gaierror:
            pass

def generate_group_vars():
    for item in hostname_vm:
        with open(os.path.join(base_path, f'{item}.yml'), 'w') as f:
            f.write('---')
            f.write('\nansible_user: ')
            f.write('\nansible_password: ')
            f.write('\nansible_become_user: ')
            f.write('\nansible_become_pass: ')
            f.write('\n\ncurrent_time: "{{ ansible_date_time.hour }}:{{ ansible_date_time.minute }}:{{ ansible_date_time.minute }}"')

generate_inventory('vm', hostname_vm)
generate_group_vars()

print(f'{base_path}/{filename} has now been generated.')