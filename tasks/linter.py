from pathlib import Path

from invoke import Context, task

from .utils import ESCAPED_REPO_PATH

NAMESPACE = "INFRAHUB-SYNC"
CURRENT_DIRECTORY = Path(__file__).parent.resolve()
MAIN_DIRECTORY = CURRENT_DIRECTORY.parent


@task(name="format")
def lint_all(context: Context) -> None:
    """This will run all linter."""

    lint_ruff(context)
    lint_pylint(context)
    lint_yaml(context)

    print(f" - [{NAMESPACE}] All linter have been executed!")


@task(name="format")
def format_all(context: Context) -> None:
    """This will run all formatter."""

    format_ruff(context)

    print(f" - [{NAMESPACE}] All formatters have been executed!")


# ----------------------------------------------------------------------------
# Linter tasks - Python
# ----------------------------------------------------------------------------
@task
def lint_pylint(context: Context) -> None:
    """This will run pylint for the specified name and Python version."""

    print(f" - [{NAMESPACE}] Check code with pylint")
    exec_cmd = f"pylint {MAIN_DIRECTORY}"
    with context.cd(ESCAPED_REPO_PATH):
        context.run(exec_cmd)


@task
def lint_ruff(context: Context) -> None:
    """This will run ruff."""

    print(f" - [{NAMESPACE}] Check code with ruff")
    exec_cmd = f"ruff format --check --diff {MAIN_DIRECTORY} &&"
    exec_cmd += f"ruff check --diff {MAIN_DIRECTORY}"
    with context.cd(ESCAPED_REPO_PATH):
        context.run(exec_cmd)


# ----------------------------------------------------------------------------
# Linter tasks - Yaml
# ----------------------------------------------------------------------------


@task
def lint_yaml(context: Context) -> None:
    """This will run yamllint to validate formatting of all yaml files."""

    print(f" - [{NAMESPACE}] Format yaml with yamllint")
    exec_cmd = "yamllint ."
    context.run(exec_cmd, pty=True)


# ----------------------------------------------------------------------------
# Formatting tasks - Python
# ----------------------------------------------------------------------------
@task
def format_ruff(context: Context) -> None:
    """This will run ruff."""

    print(f" - [{NAMESPACE}] Check code with ruff")
    exec_cmd = f"ruff format {MAIN_DIRECTORY} && "
    exec_cmd += f"ruff check --fix {MAIN_DIRECTORY}"
    with context.cd(ESCAPED_REPO_PATH):
        context.run(exec_cmd)
