Role Name
=========

network_dns_update

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

This role will update the DNS server to 8.8.8.8.

```
---

- name: untitled
  hosts: localhost
  become: true
  roles:
    - net_update_dns
```

License
-------

BSD

Author Information
------------------

- Author: Kelvin Gooding
- Date Created: 14/03/2024
