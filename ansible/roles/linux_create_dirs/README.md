Role Name
=========

linux_create_dirs

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

This role is responsible for creating new directories on Linux servers. There is a variable required in the playbook named **dir_names**. Directories that need to be created, need to nested in this variable.

```
---

- name: untitled
- hosts: localhost
-  dir_names:
    - "/home/{{ ansible_user }}/dir_1"
    - "/home/{{ ansible_user }}/dir_2"
    - "/home/{{ ansible_user }}/dir_3
   roles:
     - linux_create_dirs
```

License
-------

BSD

Author Information
------------------

- Author: Kelvin Gooding
- Date Created: 22/09/2023
