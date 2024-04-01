# README - VM_CORE

## Contents

1. [Setup](#1-setup)
2. [Ansible Scripts](#2-ansible-scripts)
3. [Shell Scripts](#3-shell-scripts)
4. [Python Scripts](#4-python-scripts)
5. [GitHib](#5-github)
6. [Docker Containers](#6-docker-containers)
7. [Cron](#7-cron)

## 1. Setup

The following packages should be installed on this server. This has been done by the ansible-playbook from the WSL server:

- Docker
- Python3
- Git
- MariaDB
- Nginx
- Jenkins
- Net-tools
- Ansible

## 2. Ansible Scripts

Transfer the following directories and files to: ```/home/`whoami`/scripts/shell```:

```
├─ shell/
│  ├─ network_info.sh
│  ├─ package_version.sh
│  ├─ server_info.sh
│  ├─ vm_core_setup.sh
```
Update the permissions of these scripts to executable:

```
chmod +x /etc/ansible/playbooks/*
```

## 3. Shell Scripts

Transfer the following directories and files to: ```/home/`whoami`/scripts/shell```:

```
├─ shell/
│  ├─ network_info.sh
│  ├─ package_version.sh
│  ├─ server_info.sh
│  ├─ vm_core_setup.sh
```
Update the permissions of these scripts to executable:

```
chmod +x /home/`whoami`/scripts/shell/*
```

Run the following script to finalise the setup/configuration for the vm_core server:

```
cd ~/scripts/shell
```

> NOTE: This is an interactive script.

```
./vm_core_setup.sh
```

## 4. Python Scripts

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

## 5. GitHub

GitHub must be set up with an SSH key's to allow the cloning of repositories from GitHub. To achieve this, follow the below steps.

> NOTE: Copy the newly generated ssh key to GitHub using the following link: https://github.com/settings/keys

## 6. Docker Containers

Run the following commands to pull the images:

- MariaDB
```
sudo docker pull mariadb:latest
```

- Nginx

```
sudo docker pull docker.io/library/nginx:latest
```

- Jenkins

```
sudo docker pull docker.io/jenkins/jenkins:lts
```
```
docker run --name docker -p 8081:8080 -d jenkins/jenkins:lts
```

## 7. Cron

The below should be added into Cron:

```
crontab -e
```
select option 2. /user/bin/vim.basic

```
## Applications

@reboot sleep 60 && /home/`whoami`/scripts/shell/jenkins_start.sh >> /etc/jenkins/jenkins_`date +\%Y\%m\%d`.log 2>&1 &

## Python Scripts

@reboot sleep 60 && python3 /home/`whoami`/scripts/python/smtp_server_restarted.py

## Ansible Playbooks

00 06 * * 7 ansible-playbook /home/`whoami`/ansible/playbooks/linux/linux_patching.yml >> /home/`whoami`/ansible-linux-patching_`date +\%Y\%m\%d`.log 2>&1

```