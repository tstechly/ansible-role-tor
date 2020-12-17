[tor](#tor)
=========

![CI](https://github.com/tstechly/ansible-role-tor/workflows/CI/badge.svg)

Install and configure tor

based mainly on 
https://computingforgeeks.com/installing-tor-browser-on-linux-mint-ubuntu/


Example Playbook
----------------

```
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: tstechly.tor```
```

Requirements
------------


Role Variables
--------------

These variables are set in `defaults/main.yml`:
```yaml
---
# By default the service is disabled
tor_service_enabled: false
tor_service_state: stopped

```


Compatibility
-------------

CentOS, Ubuntu, MacOS


Testing
-------

[Molecule](https://github.com/ansible/molecule)


```
molecule test
```

License
-------

MIT



Author Information
------------------

[Tomasz Stechly](@tstechly)