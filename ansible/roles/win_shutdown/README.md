Role Name
=========

win_shutdown

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

This role is responsible for shutting down any Windows machines which are configured.

---

- name: untitled
  hosts: all
  become: true
  roles:
    - win_shutdown
```

License
-------

BSD

Author Information
------------------

- Author: Kelvin Gooding
- Date Created: 20/09/2023
