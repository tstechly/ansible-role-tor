[tor](#tor)
=========

![CI](https://github.com/tstechly/ansible-role-tor/workflows/CI/badge.svg)

Install and configure tor

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
# defaults file for tor```


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