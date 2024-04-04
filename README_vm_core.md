# README - VM_CORE

## Contents

1. [Setup](#1-setup)
2. [GitHub](#2-github)
3. [Script](#3-script)
4. [Docker Containers](#4-docker-containers)
5. [Cron](#5-cron)

## 1. Setup

> NOTE: Before proceeding, Power off the VM, and take a Snapshot.

The following packages should be installed on this server. This has been done by the ansible-playbook from the WSL server:

- Docker
- Python3
- Git
- MariaDB
- Nginx
- Jenkins
- Net-tools
- Ansible

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
cd ~
```
```
git clone git@github.com:kelvgooding/homelab.git
```

## 3. Scripts

### Shell Scripts

The following shell scripts should be available following the cloning of the repo: https://github.com/kelvgooding/homelab/tree/main/scripts/shell

Update the permissions of these scripts to executable:

```
chmod +x /home/`whoami`/homelab/scripts/shell/*
```

Run the following script to finalise the setup/configuration for the vm_core server:

```
cd ~/homelab/scripts/shell
```

> NOTE: This is an interactive script.

```
./vm_core_setup.sh
```

### Python Scripts

The following python scripts should be available following the cloning of the repo: https://github.com/kelvgooding/homelab/tree/main/scripts/python

Run the following script to finalise the setup/configuration for the vm_core server:

> NOTE: This is an interactive script.

```
python3 ~/homelab/scripts/python/generate_config.py
```

Run the following script to create the inventory and group_vars files for Ansible to run on the vm_core server:

```
python3 ~/homelab/scripts/python/generate_inventory.py
```

### Ansible Playbooks

The following python scripts should be available following the cloning of the repo: https://github.com/kelvgooding/homelab/tree/main/ansible

Run the following script to finalise the setup/configuration for the vm_core server:

Update the permissions of these playbooks to executable:

```
chmod +x /home/`whoami`/homelab/ansible/playbooks/*
```

## 4. Docker Containers

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

## 5. Cron

The below should be added into Cron:

```
crontab -e
```
select option 2. /user/bin/vim.basic

```
## Python Scripts

@reboot sleep 60 && python3 /home/`whoami`/homelab/scripts/python/smtp_server_restarted.py

## Ansible Playbooks

00 06 * * 7 ansible-playbook /home/`whoami`/homelab/ansible/playbooks/linux/linux_patching.yml >> /home/`whoami`/ansible-linux-patching_`date +\%Y\%m\%d`.log 2>&1

```