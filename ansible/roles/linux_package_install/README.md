Role Name
=========

linux_package_install

Requirements
------------

Linux Packages:

- N/A

Role Variables
--------------

- vars_rhel_packages.yml
- vars_ubuntu_packages.yml

Dependencies
------------

N/A

Example Playbook
----------------

This role is responsible installing Linux packages. This is dependant on if the OS distrubiton is Ubuntu or Red Hat.

```
---

- name: untitled
  hosts: localhost
  become: true
  vars_files:
    - ../vars/vars_rhel_packages.yml
    - ../vars/vars_ubuntu_packages.yml
  roles:
    - linux_package_install

```

License
-------

BSD

Author Information
------------------

- Author: Kelvin Gooding
- Date Created: 20/09/2023
