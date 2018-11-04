sensu-go-ansible
================

This role allows for the deployment and management of
[Sensu Go](https://github.com/sensu/sensu-go).

Work in progress
----------------

While the initial role completely handles installing and running Sensu Go's
`sensu-agent`, `sensu-backend`, and `sensuctl` there is still a lot of work
left to do.

- [ ] Adding/Deleting/Modifying Checks

- [ ] Adding/Deleting/Modifying organizations/environments

- [ ] Adding/Deleting/Modifying roles

- [ ] Adding/Deleting/Modifying filters

- [ ] Adding/Deleting/Modifying mutators

- [ ] Adding/Deleting/Modifying handlers

- [ ] Adding/Deleting/Modifying silences

- [ ] Adding/Deleting/Modifying hooks

The current focus is adding/deleting/modifying checks. Currently, there's a 
work in progress Ansible module included in `library/` for this. Until the Sensu
Go API is versioned/documented/stable, we are wrapping `sensuctl` for our 
interactions with Sensu Go. 

If you'd like to contribute, please review [CONTRIBUTING.md](https://github.com/jaredledvina/sensu-go-ansible/blob/master/CONTRIBUTING.md) and open an issue to discuss your 
idea.

Requirements
------------

* Ansible 2.6 or higher

Role Variables
--------------

See `defaults/main.yml` for everything that's configurable.
Please note that unless you've [configured `hash_behaviour` to `merge`](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#default-hash-behaviour)
configuring any of the hash variables will **override** the entire default variable. 

Most variables expose an `_overrides: {}` variable that is merged automatically
in this role for selectively updating each variable. It's strongly recommended 
that the `overrides` variable be used.

Dependencies
------------

None

Example Playbook
----------------

```yaml
    - hosts: sensu-backend-servers
      roles:
         - role: jaredledvina.sensu-go-ansible

    - hosts: sensu-agent-severs:
      roles:
        - role: jaredledvina.sensu-go-ansible
          sensu2_components:
            - agent
          sensu2_configs_override:
            agent:
              config:
                backend-url:
                  - ws://sensu-backend-server:8081
```

Testing
-------

This Ansible role is automatically tested via TravisCI on every commit. We 
specifically test using the version of `Ansible` and `python` declared in the 
[Pipefile](https://github.com/jaredledvina/sensu-go-ansible/blob/master/Pipfile)

The following Operating Systems are automatically tested:
- [Amazon Linux](https://aws.amazon.com/amazon-linux-ami/)
- [Amazon Linux 2](https://aws.amazon.com/amazon-linux-2/)
- [CentOS - 6](https://wiki.centos.org/Manuals/ReleaseNotes/CentOS6.10)
- [CentOS - 7](https://wiki.centos.org/Manuals/ReleaseNotes/CentOS7)
- [Debian - 8 (Jessie)](https://wiki.debian.org/DebianJessie)
- [Debian - 9 (Stretch)](https://wiki.debian.org/DebianStretch)
- [Fedora - 26](https://docs.fedoraproject.org/en-US/fedora/f26/release-notes/)
- [Fedora - 27](https://docs.fedoraproject.org/en-US/fedora/f27/release-notes/)
- [Fedora - 28](https://docs.fedoraproject.org/en-US/fedora/f28/release-notes/)
- [Ubuntu - 14.04 (Trusty Tahr)](http://releases.ubuntu.com/14.04/)
- [Ubuntu - 16.04 (Xenial Xerus)](http://releases.ubuntu.com/16.04/)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)

Caveats
-------

If you are using this role with Amazon Linux or Amazon Linux 2, you must 
override the following variables on those host(s):

Amazon Linux:
```
sensu2_repos_overrides:
  yum:
    rpm: https://packagecloud.io/sensu/nightly/el/6/x86_64
    rpm-src: https://packagecloud.io/sensu/nightly/el/6/SRPMS
```
Amazon Linux 2:
```
sensu2_repos_overrides:
  yum:
    rpm: https://packagecloud.io/sensu/nightly/el/7/x86_64
    rpm-src: https://packagecloud.io/sensu/nightly/el/7/SRPMS
```


License
-------

MIT
