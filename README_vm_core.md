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

## 4. Docker / Podman Containers

Run the following commands to pull the images:

```
sudo -i
```

- MariaDB
```
sudo docker pull mariadb:latest
```

- Nginx

```
sudo docker pull docker.io/library/nginx:latest
```
### [Jenkins](https://hub.docker.com/r/jenkins/jenkins)

Jenkins is used as a CI/CD pipeline to ensure the latest version is available for use from the main branch.

1. Pull Jenkins image from Docker repository

```
docker pull jenkins/jenkins
```
2. Create a new container. This will create a container from the image which was pulled down in the previous atep.

```
sudo docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts-jdk11
```

Allow firewall port for Jenkins. This will open the port's wih the values in add ports:

```
sudo firewall-cmd --add-port=8080/tcp --permanent
sudo firewall-cmd --reload
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