import os
import sys
from shutil import rmtree

import nox
from nox.sessions import Session

# This adds directory of noxfile.py to PYTHONPATH in order to import from vfw_tgw3
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

def flake8(session: Session, toscan):
    session.run(*f"flake8 {toscan}".split(" "))


def yapf(session: Session, toscan):
    session.run(*f"yapf -r -d {toscan}".split(" "))

@nox.session(python="3")
def tests(session: Session):
    session.install("-r", "requirements.txt")
    session.install("-r", "requirements_test.txt")
    session.install("--no-use-pep517", "-e", ".")
    yapf(session, "scripts")
    flake8(session, "scripts noxfile.py")


@nox.session(python="3")
def build_docs(session: Session):
    session.install("-r", "requirements.txt")
    session.run("dbt", "seed")
    session.run("dbt", "build")
    session.run("dbt", "docs", "generate")
    # session.run("mv", "target", "docs")
