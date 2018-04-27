sensu2-ansible
==============

This role allows for the deployment of the [Sensu 2 alpha](https://github.com/sensu/sensu-go).

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
         - jaredledvina.sensu2-ansible
```

License
-------

MIT
