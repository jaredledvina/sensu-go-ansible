# Changelog

## [3.0.0](https://github.com/jaredledvina/sensu-go-ansible/tree/3.0.0) (2020-03-29)

[Full Changelog](https://github.com/jaredledvina/sensu-go-ansible/compare/2.0.0...3.0.0)

**Implemented enhancements:**

- EOL Maintenance Updates & Sensu Go Backend Initialization Support [\#337](https://github.com/jaredledvina/sensu-go-ansible/pull/337) ([jaredledvina](https://github.com/jaredledvina))

**Closed issues:**

- default user and password [\#292](https://github.com/jaredledvina/sensu-go-ansible/issues/292)
- Molecule tests are failing on docker driver [\#154](https://github.com/jaredledvina/sensu-go-ansible/issues/154)
- Reach out to flowerysong  [\#151](https://github.com/jaredledvina/sensu-go-ansible/issues/151)
- sensu-go-check module examples have invalid options [\#149](https://github.com/jaredledvina/sensu-go-ansible/issues/149)

## [2.0.0](https://github.com/jaredledvina/sensu-go-ansible/tree/2.0.0) (2019-06-22)

[Full Changelog](https://github.com/jaredledvina/sensu-go-ansible/compare/1.6.0...2.0.0)

**Implemented enhancements:**

- Tests: Use filetree to include all module tests [\#107](https://github.com/jaredledvina/sensu-go-ansible/pull/107) ([jaredledvina](https://github.com/jaredledvina))
- sensu-go-check: Add validate\_certs, cross-link docs, and more validation [\#106](https://github.com/jaredledvina/sensu-go-ansible/pull/106) ([jaredledvina](https://github.com/jaredledvina))
- sensu-go-check: Improved diffs, cleaner error handling, reduce imports [\#105](https://github.com/jaredledvina/sensu-go-ansible/pull/105) ([jaredledvina](https://github.com/jaredledvina))
- sensu-go-check: Break out SensuGo as a generic class for future modules [\#103](https://github.com/jaredledvina/sensu-go-ansible/pull/103) ([jaredledvina](https://github.com/jaredledvina))
- sensu-go-check: Only interval or cron if state is present [\#102](https://github.com/jaredledvina/sensu-go-ansible/pull/102) ([jaredledvina](https://github.com/jaredledvina))
- sensu-go-check: Support some common env fallback options [\#101](https://github.com/jaredledvina/sensu-go-ansible/pull/101) ([jaredledvina](https://github.com/jaredledvina))
- sensu-go-check: Actually fix-up diff output [\#100](https://github.com/jaredledvina/sensu-go-ansible/pull/100) ([jaredledvina](https://github.com/jaredledvina))
- sensu-go-check: Handle error -1 [\#99](https://github.com/jaredledvina/sensu-go-ansible/pull/99) ([jaredledvina](https://github.com/jaredledvina))
- sensu-go-check: Clean diffs, cleaner args [\#98](https://github.com/jaredledvina/sensu-go-ansible/pull/98) ([jaredledvina](https://github.com/jaredledvina))
- sensu-go-check: Polish and improvements [\#94](https://github.com/jaredledvina/sensu-go-ansible/pull/94) ([jaredledvina](https://github.com/jaredledvina))
- sensu-go-check: Migrate to Sensu Go API [\#93](https://github.com/jaredledvina/sensu-go-ansible/pull/93) ([jaredledvina](https://github.com/jaredledvina))
- Tests: Update Dockerfile to latest upstream version [\#91](https://github.com/jaredledvina/sensu-go-ansible/pull/91) ([jaredledvina](https://github.com/jaredledvina))
- Correctly remove old apt repo and upgrade Inspec in tests [\#89](https://github.com/jaredledvina/sensu-go-ansible/pull/89) ([jaredledvina](https://github.com/jaredledvina))

**Fixed bugs:**

- KeyError: 'labels' when using sensu\_go\_check [\#124](https://github.com/jaredledvina/sensu-go-ansible/issues/124)
- sensu-go-check failed to run [\#97](https://github.com/jaredledvina/sensu-go-ansible/issues/97)
- check name moved under metadata dictionary [\#21](https://github.com/jaredledvina/sensu-go-ansible/issues/21)
- Use ansible fact instead of yum variable for yum repos. [\#115](https://github.com/jaredledvina/sensu-go-ansible/pull/115) ([soulesn](https://github.com/soulesn))

**Closed issues:**

- Can't Add Command Line Arguments Once Check is Configured [\#45](https://github.com/jaredledvina/sensu-go-ansible/issues/45)

**Merged pull requests:**

- Cleanup for 2.0.0 release [\#132](https://github.com/jaredledvina/sensu-go-ansible/pull/132) ([jaredledvina](https://github.com/jaredledvina))
- sensu-go - Improve metadata label/annotation values [\#131](https://github.com/jaredledvina/sensu-go-ansible/pull/131) ([jaredledvina](https://github.com/jaredledvina))
- sensu\_go\_check - idempotent cron checks [\#129](https://github.com/jaredledvina/sensu-go-ansible/pull/129) ([jaredledvina](https://github.com/jaredledvina))
- Revert "Bump cryptography from 2.6.1 to 2.7" [\#116](https://github.com/jaredledvina/sensu-go-ansible/pull/116) ([jaredledvina](https://github.com/jaredledvina))
- Use the overrided config to determine when restart services [\#85](https://github.com/jaredledvina/sensu-go-ansible/pull/85) ([torrentalle](https://github.com/torrentalle))

## [1.6.0](https://github.com/jaredledvina/sensu-go-ansible/tree/1.6.0) (2019-04-19)

[Full Changelog](https://github.com/jaredledvina/sensu-go-ansible/compare/1.5.0...1.6.0)

**Merged pull requests:**

- Restart services only when component is enabled [\#83](https://github.com/jaredledvina/sensu-go-ansible/pull/83) ([torrentalle](https://github.com/torrentalle))

## [1.5.0](https://github.com/jaredledvina/sensu-go-ansible/tree/1.5.0) (2019-03-14)

[Full Changelog](https://github.com/jaredledvina/sensu-go-ansible/compare/1.4.0...1.5.0)

**Implemented enhancements:**

- Update README [\#71](https://github.com/jaredledvina/sensu-go-ansible/pull/71) ([jaredledvina](https://github.com/jaredledvina))
- Feature/improve galaxy score [\#69](https://github.com/jaredledvina/sensu-go-ansible/pull/69) ([jaredledvina](https://github.com/jaredledvina))
- Support installing packages from Sensu Community Repos [\#64](https://github.com/jaredledvina/sensu-go-ansible/pull/64) ([jaredledvina](https://github.com/jaredledvina))

## [1.4.0](https://github.com/jaredledvina/sensu-go-ansible/tree/1.4.0) (2019-02-16)

[Full Changelog](https://github.com/jaredledvina/sensu-go-ansible/compare/1.3.0...1.4.0)

**Implemented enhancements:**

- Repos - Rename prerelease to go for consistency [\#50](https://github.com/jaredledvina/sensu-go-ansible/pull/50) ([jaredledvina](https://github.com/jaredledvina))

## [1.3.0](https://github.com/jaredledvina/sensu-go-ansible/tree/1.3.0) (2019-02-08)

[Full Changelog](https://github.com/jaredledvina/sensu-go-ansible/compare/1.2.0...1.3.0)

**Implemented enhancements:**

- Add back Debian support [\#48](https://github.com/jaredledvina/sensu-go-ansible/pull/48) ([jaredledvina](https://github.com/jaredledvina))

## [1.2.0](https://github.com/jaredledvina/sensu-go-ansible/tree/1.2.0) (2019-01-29)

[Full Changelog](https://github.com/jaredledvina/sensu-go-ansible/compare/1.1.0...1.2.0)

**Implemented enhancements:**

- Add Fedora Support back & drop docs override [\#39](https://github.com/jaredledvina/sensu-go-ansible/pull/39) ([jaredledvina](https://github.com/jaredledvina))

## [1.1.0](https://github.com/jaredledvina/sensu-go-ansible/tree/1.1.0) (2018-12-23)

[Full Changelog](https://github.com/jaredledvina/sensu-go-ansible/compare/1.0.0...1.1.0)

**Merged pull requests:**

- Feature/add back ubuntu 14.04 [\#30](https://github.com/jaredledvina/sensu-go-ansible/pull/30) ([jaredledvina](https://github.com/jaredledvina))

## [1.0.0](https://github.com/jaredledvina/sensu-go-ansible/tree/1.0.0) (2018-12-16)

[Full Changelog](https://github.com/jaredledvina/sensu-go-ansible/compare/0.1.0...1.0.0)

**Implemented enhancements:**

- Feature/molecule update tests to latest setup [\#29](https://github.com/jaredledvina/sensu-go-ansible/pull/29) ([jaredledvina](https://github.com/jaredledvina))
- Switch all repos to stable channel [\#24](https://github.com/jaredledvina/sensu-go-ansible/pull/24) ([jaredledvina](https://github.com/jaredledvina))

## [0.1.0](https://github.com/jaredledvina/sensu-go-ansible/tree/0.1.0) (2018-11-05)

[Full Changelog](https://github.com/jaredledvina/sensu-go-ansible/compare/146a31b8764bb78e91e3de81bf7715495118aca1...0.1.0)

Welcome to the first release of the Sensu Go Ansible role! 🎉 

This role has been in use for a while now and is proving stable. Please checkout the [README](https://github.com/jaredledvina/sensu-go-ansible/blob/master/README.md) for some example [usage](https://github.com/jaredledvina/sensu-go-ansible/blob/master/README.md#example-playbook) and current [caveats](https://github.com/jaredledvina/sensu-go-ansible/blob/master/README.md#caveats). 

If you would like to add or see a new feature get added, please checkout [CONTRIBUTING](https://github.com/jaredledvina/sensu-go-ansible/blob/master/CONTRIBUTING.md) for details! 

**Implemented enhancements:**

- Add CentOS support [\#2](https://github.com/jaredledvina/sensu-go-ansible/issues/2)
- Update KitchenCI tests to work in TravisCI [\#1](https://github.com/jaredledvina/sensu-go-ansible/issues/1)

**Merged pull requests:**

- Grammar [\#5](https://github.com/jaredledvina/sensu-go-ansible/pull/5) ([clouseau](https://github.com/clouseau))
- Add MIT license file, include DCO, update CONTRIBUTING.md [\#4](https://github.com/jaredledvina/sensu-go-ansible/pull/4) ([jaredledvina](https://github.com/jaredledvina))
- Improve readability [\#3](https://github.com/jaredledvina/sensu-go-ansible/pull/3) ([clouseau](https://github.com/clouseau))



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
