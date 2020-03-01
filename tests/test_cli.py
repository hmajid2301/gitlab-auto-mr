import os
from collections import namedtuple

import gitlab
import pytest

from gitlab_auto_mr.cli import cli


@pytest.mark.parametrize(
    "args, exit_code",
    [
        ([], 2),
        (
            [
                "--private-token",
                "ATOKEN1234",
                "--source-branch",
                "feature/abc",
                "--gitlab-url",
                "https://gitlab.com/hmajid2301/gitlab-auto-release",
            ],
            2,
        ),
        (
            [
                "--private-token",
                "ATOKEN1234",
                "--source-branch",
                "feature/abc",
                "--gitlab-url",
                "https://gitlab.com/hmajid2301/gitlab-auto-release",
                "--wrong-args",
                "very wrong",
            ],
            2,
        ),
        (
            [
                "--source-branch",
                "feature/abc",
                "--project-id",
                21387,
                "--gitlab-url",
                "https://gitlab.com/hmajid2301/gitlab-auto-release",
            ],
            2,
        ),
        (
            [
                "--private-token",
                "ATOKEN1234",
                "--source-branch",
                "feature/abc",
                "--gitlab-url",
                "https://gitlab.com/hmajid2301/gitlab-auto-release",
                "--project-id",
                21387,
            ],
            2,
        ),
        (
            [
                "--private-token",
                "ATOKEN1234",
                "--source-branch",
                "feature/abc",
                "--gitlab-url",
                "gitlab.com/hmajid2301/gitlab-auto-release",
                "--project-id",
                21387,
                "--user-id",
                7899,
            ],
            1,
        ),
    ],
)
def test_fail_args(runner, args, exit_code):
    result = runner.invoke(cli, args)
    assert result.exit_code == exit_code


@pytest.mark.parametrize(
    "args, exception",
    [
        (
            [
                "--private-token",
                "ATOKEN1234",
                "--source-branch",
                "feature/abc",
                "--gitlab-url",
                "https://gitlab.com/hmajid2301/gitlab-auto-release",
                "--project-id",
                21387,
                "--user-id",
                7899,
            ],
            gitlab.exceptions.GitlabGetError,
        ),
        (
            [
                "--private-token",
                "ATOKEN1234",
                "--source-branch",
                "feature/abc",
                "--gitlab-url",
                "https://gitlab.com/hmajid2301/gitlab-auto-release",
                "--project-id",
                21387,
                "--user-id",
                7899,
            ],
            gitlab.exceptions.GitlabAuthenticationError,
        ),
    ],
)
def test_fail_invalid_project(mocker, runner, args, exception):
    mocker.patch("gitlab.v4.objects.ProjectManager.get", side_effect=exception)
    result = runner.invoke(cli, args)
    assert result.exit_code == 1


def test_mr_invalid_source_branch_is_target_branch(mocker, runner):
    args = [
        "--private-token",
        "ATOKEN1234",
        "--source-branch",
        "feature/abc",
        "--gitlab-url",
        "https://gitlab.com/hmajid2301/gitlab-auto-release",
        "--project-id",
        21387,
        "--user-id",
        7899,
    ]
    mock = mocker.patch("gitlab.v4.objects.ProjectManager.get")
    mock.return_value.default_branch = "feature/abc"
    result = runner.invoke(cli, args)
    assert result.exit_code == 1


def test_mr_exists(mocker, runner):
    args = [
        "--private-token",
        "ATOKEN1234",
        "--source-branch",
        "feature/abc",
        "--gitlab-url",
        "https://gitlab.com/hmajid2301/gitlab-auto-release",
        "--project-id",
        21387,
        "--user-id",
        7899,
    ]
    mock = mocker.patch("gitlab.v4.objects.ProjectManager.get")
    MR = namedtuple("MR", "source_branch")
    mock.return_value.mergerequests.list.return_value = [MR(source_branch="master"), MR(source_branch="feature/abc")]
    result = runner.invoke(cli, args)
    assert result.exit_code == 0


def test_invalid_description(mocker, runner):
    args = [
        "--private-token",
        "ATOKEN1234",
        "--source-branch",
        "feature/abc",
        "--gitlab-url",
        "https://gitlab.com/hmajid2301/gitlab-auto-release",
        "--project-id",
        21387,
        "--user-id",
        7899,
        "-d",
        "tests/data/MR.md",
    ]
    mocker.patch("gitlab.v4.objects.ProjectManager.get")
    mocker.patch("builtins.open", side_effect=OSError)
    result = runner.invoke(cli, args)
    assert result.exit_code == 0


def test_invalid_description_cannot_find(mocker, runner):
    args = [
        "--private-token",
        "ATOKEN1234",
        "--source-branch",
        "feature/abc",
        "--gitlab-url",
        "https://gitlab.com/hmajid2301/gitlab-auto-release",
        "--project-id",
        21387,
        "--user-id",
        7899,
        "-d",
        "tests/data/NotFound.md",
    ]
    mocker.patch("gitlab.v4.objects.ProjectManager.get")
    result = runner.invoke(cli, args)
    assert result.exit_code == 0


@pytest.mark.parametrize(
    "args",
    [
        (
            [
                "--private-token",
                "ATOKEN1234",
                "--source-branch",
                "feature/abc",
                "--gitlab-url",
                "https://gitlab.com/hmajid2301/gitlab-auto-release",
                "--project-id",
                21387,
                "--user-id",
                7899,
            ]
        ),
        (
            [
                "--private-token",
                "ATOKEN1234",
                "--source-branch",
                "feature/abc",
                "--gitlab-url",
                "https://gitlab.com/hmajid2301/gitlab-auto-release",
                "--project-id",
                21387,
                "--user-id",
                7899,
                "--description",
                "tests/data/MR.md",
            ]
        ),
        (
            [
                "--private-token",
                "ATOKEN1234",
                "--source-branch",
                "feature/abc",
                "--gitlab-url",
                "https://gitlab.com/hmajid2301/gitlab-auto-release",
                "--project-id",
                21387,
                "--user-id",
                7899,
                "-s",
                "-r",
                "-t",
                "master",
            ]
        ),
    ],
)
def test_success(mocker, runner, args):
    mocker.patch("gitlab.v4.objects.ProjectManager.get")
    result = runner.invoke(cli, args)
    assert result.exit_code == 0


def test_success_with_issues(mocker, runner):
    args = [
        "--private-token",
        "ATOKEN1234",
        "--source-branch",
        "feature/#12",
        "--gitlab-url",
        "https://gitlab.com/hmajid2301/gitlab-auto-release",
        "--project-id",
        21387,
        "--user-id",
        7899,
        "-s",
        "-r",
        "-t",
        "master",
        "--use-issue-name",
    ]
    mock = mocker.patch("gitlab.v4.objects.ProjectManager.get")
    Issue = namedtuple("Issue", "milestone labels")
    mock.return_value.issues.get.return_value = Issue(
        milestone={"id": "hello"}, labels=["Doing", "Core", "Priority: High"]
    )
    result = runner.invoke(cli, args)
    assert result.exit_code == 0


def test_incorrect_branch_name_issue(mocker, runner):
    args = [
        "--private-token",
        "ATOKEN1234",
        "--source-branch",
        "feature/",
        "--gitlab-url",
        "https://gitlab.com/hmajid2301/gitlab-auto-release",
        "--project-id",
        21387,
        "--user-id",
        7899,
        "-s",
        "-r",
        "-t",
        "master",
        "--use-issue-name",
    ]
    mocker.patch("gitlab.v4.objects.ProjectManager.get")
    result = runner.invoke(cli, args)
    assert result.exit_code == 0


def test_get_error_with_issues(mocker, runner):
    args = [
        "--private-token",
        "ATOKEN1234",
        "--source-branch",
        "feature/#12",
        "--gitlab-url",
        "https://gitlab.com/hmajid2301/gitlab-auto-release",
        "--project-id",
        21387,
        "--user-id",
        7899,
        "-s",
        "-r",
        "-t",
        "master",
        "--use-issue-name",
    ]
    mock = mocker.patch("gitlab.v4.objects.ProjectManager.get")
    mock.return_value.issues.get.side_effect = gitlab.exceptions.GitlabGetError
    result = runner.invoke(cli, args)
    assert result.exit_code == 0


def test_envvars(mocker, runner):
    args = [
        "-s",
        "-r",
        "-t",
        "master",
    ]
    os.environ["GITLAB_PRIVATE_TOKEN"] = "NOTATOKEN"
    os.environ["CI_PROJECT_ID"] = "81236"
    os.environ["CI_PROJECT_URL"] = "https://gitlab.com/hmajid2301/gitlab-auto-mr"
    os.environ["CI_COMMIT_REF_NAME"] = "feature/x"
    os.environ["GITLAB_USER_ID"] = "9797979"

    mocker.patch("gitlab.v4.objects.ProjectManager.get")
    result = runner.invoke(cli, args)
    assert result.exit_code == 0
