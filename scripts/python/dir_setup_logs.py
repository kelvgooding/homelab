"""
Author: Kelvin Gooding
Created: 2023-10-12
Updated: 2023-10-26
Version: 1.9
"""

# Modules

import os
import shutil
from datetime import datetime, timedelta
from pathlib import Path

# Date & Time Variables

today = datetime.today()
reduced_days = today - timedelta(days=1)

dt_current_year = today.strftime('%Y')
dt_current_month = today.strftime('%m')
dt_current_day = today.strftime('%d')
dt_full_date = today.strftime('%Y%m%d')
dt_prev_month = reduced_days.strftime('%m')
dt_prev_day = reduced_days.strftime('%Y%m%d')

# General Variables

dir_path = '/mnt/bkup'

# Script

os.chdir(dir_path)

# Create YYYY directory

if dt_current_year in os.listdir(dir_path):
    pass
else:
    os.mkdir(dt_current_year)

# Create MM directory structure

if dt_current_month in os.listdir(dir_path):
    pass
elif dt_current_day == "01":
    os.mkdir(dt_current_month)
    shutil.move(f"{dir_path}/{dt_prev_month}", f"{dir_path}/{dt_current_year}")
else:
    os.mkdir(dt_current_month)

# Creates a directory named: YYYYMMDD and YYYYMMDD/logs 

if dt_prev_day in os.listdir(dir_path):
    for log_file in Path(dir_path).glob(f"*{dt_prev_day}.log"):
        shutil.move(log_file, f"{dir_path}/{dt_prev_day}/logs")
    for csv_file in Path(dir_path).glob(f"*{dt_prev_day}.csv"):
        shutil.move(log_file, f"{dir_path}/{dt_prev_day}/db")
    shutil.move(f"{dir_path}/{dt_prev_day}", f"{dir_path}/{dt_current_month}")
    os.mkdir(dt_full_date)
    os.mkdir(f'{dir_path}/{dt_full_date}/logs')
    os.mkdir(f'{dir_path}/{dt_full_date}/db')
else:
    os.mkdir(dt_full_date)
    os.mkdir(f'{dir_path}/{dt_full_date}/logs')
    os.mkdir(f'{dir_path}/{dt_full_date}/db')
