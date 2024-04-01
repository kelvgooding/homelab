# README - VM_SNOWMOON

## Contents

1. [Setup](#1-setup)
2. [GitHub](#2-github)
3. [Scripts](#3-scripts)
4. [Cron](#4-cron)

## 1. Setup

> NOTE: Before proceeding, Power off the VM, and take a Snapshot.

The following packages should be installed on this server. This has been done by the ansible-playbook from the WSL server:

- git
- python3
- python3-pip
- sshpass
- zip
- net-tools

## 2. GitHub

GitHub must be set up with an SSH key's to allow the cloning of repositories from GitHub. To achieve this, follow the below steps.

Run the following command to generate the ssh key:

```
ssh-keygen -t rsa -b 4096
```

Run the following command to view the newly generated key:

```
cat ~/.ssh/id_rsa.pub
```

Copy the newly generated ssh key to GitHub using the following link: https://github.com/settings/keys

Run the following command to clone the homelab repo:

```
git clone git@github.com:kelvgooding/homelab.git
```

## 3. Scripts

### Shell Scripts

The following Shell scripts should be avaible in ```/home/`whoami`/homelab/scripts/shell```:

```
├─ shell/
│  ├─ network_info.sh
│  ├─ package_version.sh
│  ├─ server_info.sh
│  ├─ vm_snowmoon_setup.sh
```
Update the permissions of these scripts to executable:

```
chmod +x /home/`whoami`/homelab/scripts/shell/*
```

Run the following script to finalise the setup/configuration for the vm_snowmoon server:

```
cd ~/homelab/scripts/shell
```

> NOTE: This is an interactive script.

```
./vm_snowmoon_setup.sh
```

### Python Scripts

The following Python scripts should be avaible in ```/home/`whoami`/homelab/scripts/python```:

```
├─ python/
│  │  modules
│  │  ├─ smtp_mail.py
│  │  ├─ auth.py
│  │  ├─ __init__.py
│  ├─ dir_setup_logs.py
│  ├─ smtp_server_restarted.py
│  ├─ generate_config.py
```

Run the following script to finalise the setup/configuration for the vm_snowmoon server:

```
cd ~/homelab/scripts/python
```

> NOTE: This is an interactive script.

```
python3 generate_config.py
```

## 4. Cron

The below should be added into Cron:

```
crontab -e
```
select option 2. /user/bin/vim.basic

```
## Server Info

00 06 * * 1-7 /home/`whoami`/homelab/scripts/shell/system_info.sh > /mnt/bkup/system_info_`hostname`_`date +\%Y\%m\%d`.log 2>&1

00 06 * * 1-7 /home/`whoami`/homelab/scripts/shell/package_version.sh > /mnt/bkup/package_versions_`hostname`_`date +\%Y\%m\%d`.log 2>&1

00 06 * * 1-7 /home/`whoami`/homelab/scripts/shell/network_info.sh > /mnt/bkup/network_info_`hostname`_`date +\%Y\%m\%d`.log 2>&1

00 06 * * 1-7 sudo ufw status > /mnt/bkup/ufw_status_`hostname`_`date +\%Y\%m\%d`.log 2>&1

## Backup

00 02 * * 1-7 python3 /home/`whoami`/homelab/scripts/python/database_bkup.py

## Applications

@reboot sleep 60 && python3 /home/`whoami`/apps/contacts/app.py >> /mnt/bkup/app_contacts_`date +\%Y\%m\%d`.log 2>&1 &

@reboot sleep 60 && python3 /home/`whoami`/apps/8ball-leaderboard/app.py >> /mnt/bkup/app_8ball-leaderboard_`date +\%Y\%m\%d`.log 2>&1 &

00 00 * * 1-7 python3 /home/`whoami`/apps/crypto_spot_price/build/crypto-spot-price.py

59 23 * * 1-7 python3 /home/`whoami`/apps/crypto_spot_price/build/crypto-spot-price.py

## Python Scripts

@reboot sleep 60 && python3 /home/`whoami`/homelab/scripts/python/smtp_server_restarted.py

00 00 * * 1-7 python3 /home/`whoami`/homelab/scripts/python/dir_setup_logs.py
```