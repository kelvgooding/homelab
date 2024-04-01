# README - VM_SNOWMOON

## Contents

1. [Setup](#1-setup)
2. [Python Scripts](#5-python-scripts)
3. [Shell Scripts](#6-shell-scripts)
4. [GitHib](#9-github)
5. [Cron](#11-cron)

## 1. Setup

The following packages should be installed on this server. This has been done by the ansible-playbook from the WSL server:

- git
- python3
- python3-pip
- sshpass
- zip
- net-tools

## 2. Shell Scripts

Transfer the following directories and files to: ```/home/`whoami`/scripts/shell```:

```
├─ shell/
│  ├─ network_info.sh
│  ├─ package_version.sh
│  ├─ server_info.sh
│  ├─ vm_snowmoon_setup.sh
```
Update the permissions of these scripts to executable:

```
chmod +x /home/`whoami`/scripts/shell/*
```

Run the following script to finalise the setup/configuration for the vm_snowmoon server:

```
cd ~/scripts/shell
```

> NOTE: This is an interactive script.

```
./vm_snowmoon_setup.sh
```

## 3. Python Scripts

Transfer the following directories and files to: ```/home/`whoami`/scripts/python```:

```
├─ python/
│  │  modules
│  │  ├─ smtp_mail.py
│  │  ├─ auth.py
│  │  ├─ __init__.py
│  ├─ dir_setup_logs.py
│  ├─ smtp_server_restarted.py
```

## 4. GitHub

GitHub must be set up with an SSH key's to allow the cloning of repositories from GitHub. To achieve this, follow the below steps.

> NOTE: Copy the newly generated ssh key to GitHub using the following link: https://github.com/settings/keys

## 5. Cron

The below should be added into Cron:

```
crontab -e
```
select option 2. /user/bin/vim.basic

```
## Server Info

00 06 * * 1-7 /home/`whoami`/scripts/shell/system_info.sh > /mnt/bkup/system_info_`hostname`_`date +\%Y\%m\%d`.log 2>&1

00 06 * * 1-7 /home/`whoami`/scripts/shell/package_version.sh > /mnt/bkup/package_versions_`hostname`_`date +\%Y\%m\%d`.log 2>&1

00 06 * * 1-7 /home/`whoami`/scripts/shell/network_info.sh > /mnt/bkup/network_info_`hostname`_`date +\%Y\%m\%d`.log 2>&1

00 06 * * 1-7 sudo ufw status > /mnt/bkup/ufw_status_`hostname`_`date +\%Y\%m\%d`.log 2>&1

## Backup

00 02 * * 1-7 python3 /home/`whoami`/scripts/python/database_bkup.py

## Applications

@reboot sleep 60 && python3 /home/`whoami`/apps/contacts/app.py >> /mnt/bkup/app_contacts_`date +\%Y\%m\%d`.log 2>&1 &

@reboot sleep 60 && python3 /home/`whoami`/apps/8ball-leaderboard/app.py >> /mnt/bkup/app_8ball-leaderboard_`date +\%Y\%m\%d`.log 2>&1 &

00 00 * * 1-7 python3 /home/`whoami`/apps/crypto_spot_price/build/crypto-spot-price.py

59 23 * * 1-7 python3 /home/`whoami`/apps/crypto_spot_price/build/crypto-spot-price.py

## Python Scripts

@reboot sleep 60 && python3 /home/`whoami`/scripts/python/smtp_server_restarted.py

00 00 * * 1-7 python3 /home/`whoami`/scripts/python/dir_setup_logs.py
```

--- End of Document ---