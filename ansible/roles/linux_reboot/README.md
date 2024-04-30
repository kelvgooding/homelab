Role Name
=========

linux_reboot

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

This role is responsible for rebooting Linux servers. The reboot will work depending on which Linux Distribution is installed, either Ubuntu or RedHat in thie instance.

```
---

- name: untitled
- hosts: localhost
   roles:
     - linux_reboot
```

License
-------

BSD

Author Information
------------------

- Author: Kelvin Gooding
- Date Created: 20/09/2023
