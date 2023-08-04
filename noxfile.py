import nox


@nox.session
def format(session: nox.Session) -> None:
    session.install("ufmt", "black", "isort")
    session.run("ufmt", "format", "core")
    session.run("black", "--config=configs/.black.toml", "core", "main.py")
    session.run("isort", "--sp=configs/.isort.cfg", "core", "main.py")


@nox.session
def lint(session: nox.Session) -> None:
    session.install("ruff", "flake8")
    session.run(
        "ruff", "check", "--config=configs/.ruff.toml", "--fix", "core", "main.py"
    )
    session.run("flake8", "--config=configs/.flake8", "core", "main.py")