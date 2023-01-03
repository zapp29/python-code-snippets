import nox


@nox.session(python="3.9")
def docs(session) -> None:
    session.install("sphinx")
    session.run("sphinx-build", "docs", "docs/_build")


@nox.session
def fix(session):
    # install
    session.install("black")
    session.install("isort")
    session.install("mypy")
    # run
    session.run("black", ".")
    session.run("isort", ".")
    session.run("mypy")


@nox.session(python=["3.9", "3.10", "3.11"])
def tests(session):
    session.run("poetry", "install", external=True)
    session.run("pytest")
