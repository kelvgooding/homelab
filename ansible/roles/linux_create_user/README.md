Role Name
=========

linux_create_user

Requirements
------------

Linux Packages:

- N/A

Role Variables
--------------

- vars_create_users.yml

Dependencies
------------

N/A

Example Playbook
----------------

This role is responsible fpr create a new user on the required Linux server.

```
---

- name: vm-001-prod - Server setup & configuration
  hosts: localhost
  become: true
  vars_files:
    - ../../vars/vars_create_users.yml
  roles:
    - linux_create_user

```

License
-------

BSD

Author Information
------------------

- Author: Kelvin Gooding
- Date Created: 05/07/2024
