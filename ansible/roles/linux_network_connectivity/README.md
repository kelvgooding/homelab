Role Name
=========

linux_network_connectivity

Requirements
------------

N/A

Role Variables
--------------

N/A

Dependencies
------------

N/A

Example Playbook
----------------

This role is responsible checking the network connectivity of all Linux machines.

---

- name: untitled
  hosts: all
  become: true
  roles:
    - linux_network_connectivity
```

License
-------

BSD

Author Information
------------------

- Author: Kelvin Gooding
- Date Created: 19/09/2023
