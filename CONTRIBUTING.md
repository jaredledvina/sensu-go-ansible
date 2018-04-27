# Getting started

It's *strongly* encouraged that everyone who works on this repository configures
their local development environment with the following procedure:

1. Install `pipenv`: https://docs.pipenv.org/install/
2. Install this repo's development dependencies: `pipenv install --two --dev`
3. Install Docker: https://docs.docker.com/install/
4. Verify that Docker is running: `docker ps`
5. Verify that you can perform local integration testing: `pipenv run molecule test`


# Writing integration tests

This Ansible role is tested automatically via `molecule` on TravisCI. Integration
tests are the corner-stone to ensuring that all future changes are backwards
compatible and function as expected across all operating systems.

Currently, we use [Inspec](https://www.inspec.io/) as the integration tests
verifier. The eventual goal is that all Sensu 2 configuration management repo's
consume a standard Inspec profile that ensures that across all of the individual
tools, each is satisfying a baseline configuration standard.


All Inspec tests live in `molecule/default/tests`. If you followed the above
environment setup, you can execute the tests with `pipenv run molecule verify`.


# Pull Request Requirements

All Pull Requests to this Ansible role are required to have:
* New or updated Inspec integration tests validating the change
* Passed all existing and new integrations tests in TravisCI
* Updated the `CHANGELOG.md` with information about the change

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
the TDD mindset. Start by updating the integration tests such that they fail due
to the new feature/change not being present. Then, update the role with the
required change. Lastly, verify that the change actually did what you wanted and
now the tests pass.

