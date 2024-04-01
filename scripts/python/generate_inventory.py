"""
Author: Kelv Gooding
Created: 2024-02-03
Updated: 2024-02-07
Version: 1.1
Description: A script to create the inventory file for Ansible.
"""

# Modules

import socket
import os

# Variables

base_path = '/etc/ansible'
filename = 'inventory'
abs_path = os.path.join(base_path, filename)

# Arrays

hostname_vm = [
    'snowmoon',
]

# Script

# Remove inventory file if this already exists

os.remove(abs_path)

def gather_ips(inventory_group, server_group):

    # Generate Inventory file

    with open(abs_path, 'a') as f:
        try:
            for hostname in server_group:

                # Check if IP can be obtained

                socket.gethostbyname(hostname)

                # Write hostname and IP address to inventory file

                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("8.8.8.8", 80))
                f.write(f'[{hostname}]\n')
                f.write(f'{s.getsockname()[0]}\n\n')

            # Create a group for the hosts

            f.write(f'[{inventory_group}:children]\n')
            for a in server_group:
                f.write(f'{a}\n')
            f.write('\n')
    
        # If IP cannot be found, continue to iterate

        except socket.gaierror:
            pass

gather_ips('vm', hostname_vm)

print(f'{base_path}/{filename} has now been generated')
