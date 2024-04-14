# README - WSL

## Contents

1. [Installation](#1-installation)
2. [Setup](#2-setup)
3. [GitHub](#3-github)
4. [Ansible Playbooks](#5-ansible-playbooks)

## 1. Installation

Before installing WSL, ensure that the update has been done so there are no errors when setting up:

Launch Powershell

Run the following commands:

```
wsl --update
```
Install the Ubuntu distribution:
```
wsl --install -d ubuntu
```
Once installed and username/password has been created, use the following command to clear any launch scripts:
```
touch /home/`whoami`/.hushlogin
```

## 2. Setup

Log into server.

Update packages:

```
sudo apt update -y
```

Install Ansible:

```
sudo apt install -y ansible sshpass
```

## 3. GitHub

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

## 4. Ansible Playbooks

Before running any ansible playbooks, run the following python scripts. This will generate the inventory file for ansible:

> NOTE: Amend the array name within this script if the server names are changed.

```
python3 ~/homelab/scripts/python/generate_inventory.py
```

Edit the following files inside of the following directory to include the user and root credentials the server(s). These files are generated from running generate_inventory.py:

```
cd ~/homelab/ansible/group_vars
```

Run the following playbook to ensure that a connection can be establisted to the server(s):

```
cd ~/homelab/ansible/playbooks
```

```
ansible-playbook all_network_connectivity.yml
```

### vm_snowmoon

Run the following command to check the playbook will run successfully:

```
cd ~/homelab/ansible/playbooks/wsl
```
```
nohup ansible-playbook wsl_setup_vm_snowmoon.yml --check >> ~/homelab/logs/ansible_playbook_setup_vm_snowmoon_check_`date +\%Y\%m\%d_\%H\%M\%S`.log 2>&1 &
```

The logs can be found in the following location:

```
cd ~/homelab/logs
```
```
cat $(ls -t | head -n1)
```

If sucessful, run the following command to setup and configuration of vm_snowmoon:

```
cd ~/homelab/ansible/playbooks/wsl
```
```
nohup ansible-playbook wsl_setup_vm_snowmoon.yml >> ~/homelab/logs/ansible_playbook_setup_vm_snowmoon_`date +\%Y\%m\%d_\%H\%M\%S`.log 2>&1 &
```

The logs can be found in the following location:

```
cd ~/homelab/logs
```
```
cat $(ls -t | head -n1)
```

Once this playbook is complete, the configuration can be found here:

* [vm_snowmoon](README_vm_snowmoon.md)

### vm_core

Run the following command to check the playbook will run successfully:

```
cd ~/homelab/ansible/playbooks/wsl
```
```
nohup ansible-playbook wsl_setup_vm_core.yml --check >> ~/homelab/logs/ansible_playbook_setup_vm_core_check_`date +\%Y\%m\%d_\%H\%M\%S`.log 2>&1 &
```

The logs can be found in the following location:

```
cd ~/homelab/logs
```
```
cat $(ls -t | head -n1)
```

If successful, run the following command to setup and configuration of vm_core:

```
cd ~/homelab/ansible/playbooks/wsl
```
```
nohup ansible-playbook wsl_setup_vm_core.yml >> ~/homelab/logs/ansible_playbook_setup_vm_core_`date +\%Y\%m\%d_\%H\%M\%S`.log 2>&1 &
```

The logs can be found in the following location:

```
cd ~/homelab/logs
```
```
cat $(ls -t | head -n1)
```

Once this playbook is complete, the configuration can be found here:

* [vm_core](README_vm_core.md)
