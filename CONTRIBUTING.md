# Getting started

It's **strongly** encouraged that everyone who works on this repository configures
their local development environment with the following procedure:

1. Install `pipenv`: https://docs.pipenv.org/install/
2. Install this repo's development dependencies: `pipenv install --two --dev`
3. Install Docker: https://docs.docker.com/install/
4. Verify that Docker is running: `docker ps`
5. Verify that you can perform local integration testing: `pipenv run molecule test`

# Contributing

1. Open an issue to describe your proposed improvement or feature
2. Fork https://github.com/jaredledvina/sensu-go-ansible and clone your fork to your workstation
3. Create your feature branch (`git checkout -b feature/my-new-feature`)
4. Commit your changes with a [DCO Signed-off-by statement](#dco) (`git commit --signoff`)
5. Push your feature branch (`git push origin feature/my-new-feature`)
6. [Create a Pull Request from your fork](https://help.github.com/articles/creating-a-pull-request-from-a-fork/)

## DCO

To make a good faith effort to ensure the criteria of the MIT License
are met this repository requires the Developer Certificate of Origin (DCO)
process to be followed.

The DCO is an attestation attached to every contribution made by every
developer. In the commit message of the contribution, the developer
simply adds a `Signed-off-by` statement and thereby agrees to the DCO,
which you can find below or at http://developercertificate.org/.

```
Developer Certificate of Origin
Version 1.1

Copyright (C) 2004, 2006 The Linux Foundation and its contributors.
1 Letterman Drive
Suite D4700
San Francisco, CA, 94129

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.


Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.
```

# Writing integration tests

This Ansible role is tested automatically via
[`molecule`](https://github.com/ansible/molecule) on TravisCI. Integration
tests are the corner-stone to ensuring that all future changes are backwards
compatible and function as expected across all operating systems.

Currently, we use [Inspec](https://www.inspec.io/) as the integration tests
verifier. The eventual goal is that all Sensu Go configuration management repo's
consume a standard Inspec profile that ensures that across all of the individual
tools, each is satisfying a baseline configuration standard.


All Inspec tests live in `molecule/shared/tests`. If you followed the above
environment setup, you can execute the tests with `pipenv run molecule verify`.


# Pull Request Requirements

All Pull Requests to this Ansible role are required to have:
* New or updated Inspec integration tests validating the change
* Passed all existing and new integrations tests in TravisCI
* An accurate title and description, which will be used in the CHANGELOG

# Design Considerations

This Ansible role is written in an attempt to be as flexible as possible. You
will notice in `defaults/main.yml` that this Ansible role makes use for extensive
YAML dictionaries allow with `_override` fails. This design allows for basic
YAML variable merging behaviour without requiring users to globally enable
merging for their entire Ansible run.

By default, the goal is that any setting that could be configurable should be.
This ends up requiring more work to extract out various configuration pieces but,
results in an extremely flexible user experience. When adding more functionality,
please keep this in mind.

When it comes to testing, it's highly recommended to approach the new change with
the [TDD](https://en.wikipedia.org/wiki/Test-driven_development)
mindset. Start by updating the integration tests such that they fail due
to the new feature/change not being present. Then, update the role with the
required change. Lastly, verify that the change actually did what you wanted and
now the tests pass.
