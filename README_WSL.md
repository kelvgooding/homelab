# README - WSL

## Contents

1. [Installation](#1-installation)
2. [Setup](#2-setup)
3. [Ansible](#3-ansible)
4. [Soft Links](#4-soft-links)
5. [Configuration Management](#5-configuration-management)

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

## 3. Ansible

The **Ansible** directiory needs to be added to ```/etc/ansible```

```
mkdir /etc/ansible
```

Change the owner of the /etc/ansible directory:

```
sudo chown `whoami`:`whoami` /etc/ansible
```

Transfer the following files to the server:

```
ansible/
├─ group_vars/
│  ├─ kelv_laptop
│  ├─ kelv_pc
│  ├─ vm_snowmoon
│  ├─ vm_core
├─ playbooks/
│  ├─ all_network_connectivity.yml
│  ├─ all_os_check.yml
│  ├─ archived
│  ├─ in_progress
│  ├─ windows
│  │  ├─ win_create_user.yml
│  │  ├─ win_map_network_drive.yml
│  │  ├─ win_reboot.yml
│  │  ├─ win_setup_desktop.yml
│  │  ├─ win_setup_downloads.yml
│  │  ├─ win_setup_explorer.yml
│  │  ├─ win_setup_full.yml
│  │  ├─ win_setup_settings.yml
│  │  ├─ win_setup_taskbar.yml
│  │  ├─ win_shutdown.yml
│  ├─linux
│  │  ├─ linux_package_install.yml
│  │  ├─ linux_patching.yml
│  │  ├─ linux_reboot.yml
│  ├─pip
│  │  ├─ pip_install_packages.yml
│  ├─wsl
│  │  ├─ wsl_setup_vm_core.yml
│  │  ├─ wsl_setup_vm_snowmoon.yml
├─ roles/
│  ├─ linux_create_dirs
│  ├─ linux_network_connectivity
│  ├─ linux_package_install
│  ├─ linux_reboot
│  ├─ linux_update
│  ├─ linux_upgrade
│  ├─ network_dns_update
│  ├─ os_distribution
│  ├─ pip_package_install
│  ├─ url_file_download
│  ├─ win_network_connectivity
│  ├─ win_reboot
│  ├─ win_shutdown
├─ ansible.cfg
├─ inventory
```

## 4. Soft Links

Run the following commands to create soft links:

```
ln -s /etc/ansible /home/`whoami`
```

## 5. Ansible Playbooks

### vm_snowmoon

Run the following command to check the playbook will run successfully:

```
cd ~/ansible/playbooks/wsl
```

```
nohup ansible-playbook wsl_setup_vm_snowmoon.yml --check >> /etc/ansible/logs/ansible_playbook_setup_vm_snowmoon_check_`date +\%Y\%m\%d_\%H\%M\%S`.log 2>&1 &
```

If sucessful, run the following command to setup and configuration of vm_snowmoon:

```
nohup ansible-playbook wsl_setup_vm_snowmoon.yml >> /etc/ansible/logs/ansible_playbook_setup_vm_snowmoon_`date +\%Y\%m\%d_\%H\%M\%S`.log 2>&1 &
```

Once this playbook is complete, the configuration can be found here:

* [vm_snowmoon](README_vm_snowmoon.md)

### vm_core

```
cd ~/ansible/playbooks/wsl
```

Run the following command to check the playbook will run successfully:

```
nohup ansible-playbook wsl_setup_vm_core.yml --check >> /etc/ansible/logs/ansible_playbook_setup_vm_core_check_`date +\%Y\%m\%d_\%H\%M\%S`.log 2>&1 &
```

If successful, run the following command to setup and configuration of vm_core:

```
nohup ansible-playbook wsl_setup_vm_core.yml >> /etc/ansible/logs/ansible_playbook_setup_vm_core_`date +\%Y\%m\%d_\%H\%M\%S`.log 2>&1 &
```

Once this playbook is complete, the configuration can be found here:

* [vm_core](README_vm_core.md)