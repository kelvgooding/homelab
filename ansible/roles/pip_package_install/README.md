Role Name
=========

pip_package_install

Requirements
------------

N/A

Role Variables
--------------

vars_pip_packages.yml

Dependencies
------------

N/A

Example Playbook
----------------

This role will install pip packages onto the server.

```
---

- name: untitled
  hosts: localhost
  become: true
  vars_files:
    - ../vars/vars_pip_packages.yml
  roles:
    - pip_package_install
```

License
-------

BSD

Author Information
------------------

- Author: Kelvin Gooding
- Date Created: 12/03/2024
