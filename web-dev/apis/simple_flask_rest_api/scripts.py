import subprocess


def tests():
    subprocess.run(["nox", "-s", "tests"])


def fix():
    subprocess.run(["nox", "-s", "fix"])


def docs():
    subprocess.run(["nox", "-s", "docs"])


def app():
    subprocess.run(["flask", "--app", "simple_flask_rest_api", "run"])


def debug():
    subprocess.run(["flask", "--app", "simple_flask_rest_api", "--debug", "run"])


def init():
    subprocess.run(["flask", "--app", "simple_flask_rest_api", "init-db"])
