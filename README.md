sensu-go-ansible
==============

This role allows for the deployment and management of
[Sensu 2](https://github.com/sensu/sensu-go).

Requirements
------------

* Ansible 2.5 or higher

Role Variables
--------------

See `defaults/main.yml` for everything that's configurable.

Dependencies
------------

None

Example Playbook
----------------

```
    - hosts: servers
      roles:
         - jaredledvina.sensu-go-ansible
```

License
-------

MIT
