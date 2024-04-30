Role Name
=========

win_network_connectivity

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

This role is responsible checking the network connectivity of all windows machines.

---

- name: untitled
  hosts: all
  become: true
  roles:
    - win_network_connectivity
```

License
-------

BSD

Author Information
------------------

- Author: Kelvin Gooding
- Date Created: 20/09/2023
