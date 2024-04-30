Role Name
=========

linux_firewall_allow

Requirements
------------

Linux Packages:

- N/A

Role Variables
--------------

vars_port_numbers

Dependencies
------------

N/A

Example Playbook
----------------

The role is responsible for allowing inbound/outbound connections by opening firewall ports on the Linux machine.

---

- name: vm-core - Server setup & configuration
  hosts: vm-core
  become: true
  vars_files:
    - ../vars/vars_port_numbers
  roles:
    - linux_firewall_allow

License
-------

BSD

Author Information
------------------

- Author: Kelvin Gooding
- Date Created: 13/04/2024
