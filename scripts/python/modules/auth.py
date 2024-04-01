"""
Author: Kelvin Gooding
Created: 2022-10-25
Updated: 2024-03-07
Version: 1.1
"""

# Modules

from configparser import ConfigParser
import os

config = ConfigParser()
config.read(f'/home/{os.getlogin()}/.config.ini')

smtp_auth = {
    'server' : config.get('SMTP', 'SMTP_SERVER'),
    'port' : config.get('SMTP', 'SMTP_PORT'),
    'email' : config.get('SMTP', 'SMTP_EMAIL'),
    'password' : config.get('SMTP', 'SMTP_PASSWORD'),
    }
