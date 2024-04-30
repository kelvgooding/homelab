Role Name
=========

linux_update

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

This role is responsible for patching Linux servers. This is dependant on if the OS distrubution is Ubuntu, or Red Hat.

```
---

- name: Security - patching linux servers
  hosts: localhost
  become: true
  roles:
    - linux_update
```

License
-------

BSD

Author Information
------------------

- Author: Kelvin Gooding
- Date Created: 19/09/2023
