"""
Author: Kelvin Gooding
Created: 2024-04-02
Updated: 2024-04-02
Version: 1.0
"""

# Modules

import os

path = f'/home/{os.getlogin()}'

server = input('Enter SMTP server: ')
mailbox = input('Enter Mailbox: ')
password = input('Enter Mailbox Password: ')

print(f'\nA new file has now been generated - {path}/config.ini')

with open(f'{path}/config.ini', 'w') as f:
    f.write('[SMTP]')
    f.write(f'\nSMTP_SERVER = {server}')
    f.write(f'\nSMTP_PORT = 587')
    f.write(f'\nSMTP_EMAIL = {mailbox}')
    f.write(f'\nSMTP_PASSWORD = {password}')