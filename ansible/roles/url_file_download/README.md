Role Name
=========

url_file_download

Requirements
------------

N/A

Role Variables
--------------

{{ dir_names }}

Dependencies
------------

N/A

Example Playbook
----------------

This role will download packages or files using a URL.

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
- Date Created: 16/01/2024
