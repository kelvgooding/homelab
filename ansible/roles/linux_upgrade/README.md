Role Name
=========

linux_upgrade

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

- name: Security - patching linux servers
  hosts: localhost
  become: true
  roles:
    - linux_upgrade
```

License
-------

BSD

Author Information
------------------

- Author: Kelvin Gooding
- Date Created: 19/09/2023 