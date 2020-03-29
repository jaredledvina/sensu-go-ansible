sensu-go-ansible
================

[![Build Status](https://img.shields.io/travis/com/jaredledvina/sensu-go-ansible/master.svg)](https://travis-ci.com/jaredledvina/sensu-go-ansible)
[![GitHub release](https://img.shields.io/github/release/jaredledvina/sensu-go-ansible.svg)](https://github.com/jaredledvina/sensu-go-ansible/releases/latest)
[![License](https://img.shields.io/github/license/jaredledvina/sensu-go-ansible.svg)](https://github.com/jaredledvina/sensu-go-ansible)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fjaredledvina%2Fsensu-go-ansible.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fjaredledvina%2Fsensu-go-ansible?ref=badge_shield)

This role allows for the deployment and management of
[Sensu Go](https://github.com/sensu/sensu-go). 

The official Sensu supported Ansible Collection can be found here: https://github.com/sensu/sensu-go-ansible

If you'd like to contribute, please review [CONTRIBUTING.md](https://github.com/jaredledvina/sensu-go-ansible/blob/master/CONTRIBUTING.md) and open an issue to discuss your
idea.

Requirements
------------

* [Ansible 2.9](https://docs.ansible.com/ansible/2.9/installation_guide/intro_installation.html)

Role Variables
--------------

See [`defaults/main.yml`](https://github.com/jaredledvina/sensu-go-ansible/blob/master/defaults/main.yml)
for everything that's configurable. If any of the options are unclear, please 
[file an issue](https://github.com/jaredledvina/sensu-go-ansible/issues/new)!

Please note that unless you've [configured `hash_behaviour` to `merge`](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#default-hash-behaviour)
configuring any of the hash variables will **override** the entire default variable.

Most variables expose an `_overrides: {}` variable that is merged automatically
in this role for selectively updating each variable. It's strongly recommended
that the `_overrides` variable be used.

Dependencies
------------

None

Example Playbook
----------------

The following example will configure the host in the hostgroup 
`sensu-backend-server` to be configured with both `sensu-backend` and 
`sensu-agent`. This host will also get the `sensuctl` CLI tool for further 
management of Sensu Go. 

The hosts in `sensu-agent-severs` will only get the `sensu-agent` install and
will have the `sensu-agent`'s configuration option for `backend-url` 
overriden to `ws://sensu-backend-server:8081`. 

For more information on the availible configuration options, checkout the upstream docs for 
[`sensu-backend`](https://docs.sensu.io/sensu-go/latest/reference/backend/#general-configuration-flags) and 
[`sensu-agent`](https://docs.sensu.io/sensu-go/latest/reference/agent/#general-configuration-flags).

```yaml
---
-
  hosts: sensu-backend-server
  become: yes
  roles:
    - role: jaredledvina.sensu_go_ansible
-
  hosts: sensu-agent-severs
  roles:
    - role: jaredledvina.sensu_go_ansible
      sensu_go_components:
        - agent
      sensu_go_configs_override:
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
- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Fedora - 30](https://docs.fedoraproject.org/en-US/fedora/f30/release-notes/)
- [Fedora - 31](https://docs.fedoraproject.org/en-US/fedora/f31/release-notes/)
- [Ubuntu - 16.04 (Xenial Xerus)](https://releases.ubuntu.com/16.04/)
- [Ubuntu - 18.04 (Bionic Beaver)](https://releases.ubuntu.com/18.04/)


Custom Modules
--------------

This role includes the following [custom modules](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html#embedding-modules-and-plugins-in-roles):
- [sensu-go-check](https://github.com/jaredledvina/sensu-go-ansible/blob/master/library/sensu_go_check.py)

At this time, these modules are in [`preview`](https://docs.ansible.com/ansible/2.5/dev_guide/developing_modules_documenting.html#ansible-metadata-block)
status and may be subject to breaking changes. However, effort will be 
put in to attempt to not break the them, if possible. Please ensure you 
review the [CHANGELOG](https://github.com/jaredledvina/sensu-go-ansible/blob/master/CHANGELOG.md) when upgrading.

As described in the [upstream documentation](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html#embedding-modules-and-plugins-in-roles),
to use the included custom modules, you must first include this role prior to 
calling the modules. After this role has been included once, they will be 
availble to subsequent plays/roles.

Currently, documentation for each module is in the `DOCUMENTATION` block in 
each modules source. Once the modules stabalized, they may be PR'ed upstream
to the Ansible project.

Caveats
-------

If you are using this role with Amazon Linux or Amazon Linux 2, you must
override the following variables on those host(s):

Amazon Linux:
```yaml
sensu_go_repos_overrides:
  yum:
    rpm: https://packagecloud.io/sensu/stable/el/6/x86_64
    rpm-src: https://packagecloud.io/sensu/stable/el/6/SRPMS
sensu_go_community_repos_overrides:
  yum:
    rpm: https://packagecloud.io/sensu/community/el/6/x86_64
    rpm-src: https://packagecloud.io/sensu/community/el/6/SRPMS
```

Amazon Linux 2:
```yaml
sensu_go_repos_overrides:
  yum:
    rpm: https://packagecloud.io/sensu/stable/el/7/x86_64
    rpm-src: https://packagecloud.io/sensu/stable/el/7/SRPMS
sensu_go_community_repos_overrides:
  yum:
    rpm: https://packagecloud.io/sensu/community/el/7/x86_64
    rpm-src: https://packagecloud.io/sensu/community/el/7/SRPMS
```

If you are using this role with Debian 8, 9, or 10 hosts, you must overide the 
following variable:

```yaml
sensu_go_manage_community_repo: false
```

This is due to Debian packages not being updated to the community repos 
pending the resolution of https://github.com/sensu/sensu-plugins-omnibus/issues/3
```

License
-------

[MIT](https://github.com/jaredledvina/sensu-go-ansible/blob/master/LICENSE)


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fjaredledvina%2Fsensu-go-ansible.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fjaredledvina%2Fsensu-go-ansible?ref=badge_large)
