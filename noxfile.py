import os
import sys

import nox
from nox.sessions import Session

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))


def install(session: Session):
    session.install("-r", "requirements.txt")


def dbt_run(session: Session, *dbt_args: str, local_profile: bool = False):
    args = ["dbt", *dbt_args]
    if local_profile:
        args.extend(["--profiles-dir", "."])
    session.run(*args)


def flake8(session: Session, toscan: str):
    session.run("flake8", *toscan.split())


def yapf(session: Session, toscan: str):
    session.run("yapf", "-r", "-d", *toscan.split())


@nox.session(python="3")
def tests(session: Session):
    local_profile = "--local-profile" in session.posargs

    install(session)
    yapf(session, "scripts")
    flake8(session, "scripts noxfile.py")

    dbt_run(session, "seed", local_profile=local_profile)
    dbt_run(session, "test", local_profile=local_profile)

    # session.run("pytest")


@nox.session(python="3")
def build_docs(session: Session):
    local_profile = "--local-profile" in session.posargs

    install(session)
    dbt_run(session, "deps", local_profile=local_profile)
    dbt_run(session, "seed", local_profile=local_profile)
    dbt_run(session, "build", local_profile=local_profile)
    dbt_run(session, "docs", "generate", local_profile=local_profile)
