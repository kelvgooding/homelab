Role Name
=========

linux_user_permissions

Requirements
------------

Linux Packages:

- N/A

Role Variables
--------------

N/A

Dependencies
------------

N/A

Example Playbook
----------------

This role is responsible for automatically downloads the latest version of the packages and replaces the old version package by installing the new one.. This is dependant on if the OS distrubution is Ubuntu, or Red Hat.

```
---

- name: untitled
  hosts: localhost
  become: true
  roles:
    - linux_user_permissions
```

License
-------

BSD

Author Information
------------------

- Author: Kelvin Gooding
- Date Created: 28/03/2024
