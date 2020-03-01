# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- unit tests with 100% code coverage.
- `dev-requirements.txt` for development requirements such as black.
- `isort` to sort imports.
- `coverage` to detect code coverage from unit tests.
- `coverage` job in `.gitlab-ci.yml`.
- Publish to staging pypi first.

### Changed
- `makefile` to `Makefile`.
- `MANIFEST.in` with recommended changes from `check-manifest`.
- `README.rst` added a coverage badge.
- `code-formatter` name in `tox.ini` to.
- `docker` publish job to pre-publish only on release tags.
- Update README.rst, setup development environment env.

### Removed
- `docs` folder.

## [1.1.3] - 2019-10-26
### Changed
- Used predefined variables in `gitlab-ci`.
- Removed git strategy doesn't make sense if we're using a merge request file.

## [1.1.2] - 2019-10-26
### Fixed
- Updated docs with new arguments.
- Missing tox target for `make virtualenv` (`:dev`).

## [1.1.1] - 2019-10-26
### Changed 
- Check only opened MRs fixes (from MR #1).

## [1.1.0] - 2019-10-26
### Changed
- Updated README.rst, to include more useful information, about predefined variables.

### Fixed
- Tool only worked on GitLabs urls that were subdomains, now will work on any just specify gitlab-url.

### Removed
- Repeated sections from README.rst.

## [1.0.1] - 2019-07-30
### Changed
- README.rst to include new short params i.e. -t instead --target. 

## [1.0.0] - 2019-07-30
### Removed
- Some env variables as options for cli input. Shouldn't be using env variables for all cli inputs. 

## [0.6.1] - 2019-07-29
### Changed
- Changed any reference to hmajid2301/gitlab-auto-release to gitlab-automation-toolkit/gitlab-auto-release.

## [0.6.0] - 2019-07-24
### Added
- Allow Collaboration option which if set, allow commits from members who can merge to the target branch. 

### Changed
- `code-formatter` to include `{posargs}` so we can use it to format our code, and also to check it in the same target.

### Fixed
- Mock import `gitlab` in `conf.py`.
- Master doc file not found error on `readthedocs`, explicity added it into `conf.py`.

### Removed
- `m2r` library as a dependency for docs (Sphinx).
- `code-formatter-check` target in tox.

## [0.5.2] - 2019-05-05
### Fixed
- To set milestone should be `id` not `iid`.

## [0.5.1] - 2019-04-30
### Changed
- Function from `is_mr_valid` to `check_if_mr_is_valid`.

### Fixed
- Exits with an error (1) if MR exists already, should exit without an error (0).

## [0.5.0] - 2019-04-30
### Added
- Tag docker image with version from `setup.py`.

### Fixed
- Wrong url returned we only want host, we don't need API url.
- Should be interacting like an object `mr.source_branch` instead of as a dict i.e. `mr["source_branch"]`
- Use only `issue_number` i.e. `4` instead of `#4`.

## [0.4.1] - 2019-04-30
### Fixed
- Typo `projects` instead of `project` for gitlab object.

## [0.4.0] - 2019-04-30
### Changed
  - Using `python-gitlab` library instead of using `requests` to make HTTP API requests to Gitlab. This has helped simplify the code.

### Fixed
  - Don't exit with 1 status code if issue doesn't exist in branch name.

## [0.3.1] - 2019-04-29
### Fixed
  - If issue number doesn't exist on project labels and milestone will be none. Check if response from API call contains this data.
  - Multiple `here's` in `README.rst` raising error when pushing to pypi.

## [0.3.0] - 2019-04-29
### Changed
  - `DESCRIPTION` option now accepts a file as input rather than a string.

## [0.2.7] - 2019-04-13
### Changed
  - Moved changelog back into rst.

## [0.2.6] - 2019-04-12
### Fixed
  - Removed post1.

### Changed
  - Moved changelog to separate file.

## [0.2.5] - 2019-04-12
### Fixed
  - README badges links.

## [0.2.4] - 2019-04-12
### Fixed
  - README badges include links.

## [0.2.3] - 2019-04-12
### Added
  - Tox to the project.
  - readthedocs integration.

### Changed
  - README to include readthedocs badge.

## [0.2.2post1] - 2019-04-11
### Added
  - Updated a README with a Changelog.

## [0.2.2] - 2019-04-10
### Fixed
  - Formatting error in README.

## [0.2.1] - 2019-04-10
### Fixed
  - Formatting error in README.

## [0.2.0] - 2019-04-10
### Added
  - Using black as code formatter.
  - Added new argument, `--use-issue-name` which is adds settings from issue such as labels to the MR.

## [0.1.4] - 2019-03-16
### Changed
  - Updated README with new badges and better installation instructions.

## [0.1.3] - 2019-03-16
### Fixed
  - Exit with 0 value if MR already exists.

## [0.1.2] - 2019-03-16
### Fixed
  - Documentation using `gitlab-auto-merge-request` instead of `gitlab-auto-mr`.

## [0.1.0] - 2019-03-16
### Added
  - Initial Release.

[Unreleased]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-release/-/compare/release%2F1.1.3...master
[1.1.3]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F1.1.2...release%2F1.1.3
[1.1.2]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F1.1.1...release%2F1.1.2
[1.1.1]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F1.1.0...release%2F1.1.1
[1.1.0]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F1.0.1...release%2F1.1.0
[1.0.1]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F1.0.0...release%2F1.0.1
[1.0.0]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F0.6.1...release%2F1.0.0
[0.6.1]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F0.6.0...release%2F0.6.1
[0.6.0]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F0.5.2...release%2F0.6.0
[0.5.2]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F0.5.1...release%2F0.5.2
[0.5.1]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F0.5.0...release%2F0.5.1
[0.5.0]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F0.4.1...release%2F0.5.0
[0.4.1]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F0.4.0...release%2F0.4.1
[0.4.0]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F0.3.1...release%2F0.4.0
[0.3.1]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F0.3.0...release%2F0.3.1
[0.3.0]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F0.2.7...release%2F0.3.0
[0.2.7]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F0.2.6...release%2F0.2.7
[0.2.6]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F0.2.5...release%2F0.2.6
[0.2.5]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F0.2.4...release%2F0.2.5
[0.2.4]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F0.2.3...release%2F0.2.4
[0.2.3]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F0.2.2post1...release%2F0.2.3
[0.2.2post1]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F0.2.2...release%2F0.2.2post1
[0.2.2]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F0.2.1...release%2F0.2.2
[0.2.1]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F0.2.0...release%2F0.2.1
[0.2.0]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F0.1.4...release%2F0.2.0
[0.1.4]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F0.1.3...release%2F0.1.4
[0.1.3]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F0.1.2...release%2F0.1.3
[0.1.2]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr/-/compare/release%2F0.1.0...release%2F0.1.2
[0.1.0]: https://gitlab.com/gitlab-automation-toolkit/gitlab-auto-mr-issue/-/tags/release%2F0.1.