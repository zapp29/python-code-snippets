import subprocess

def app():
    subprocess.run(["uvicorn", "main:app", "--reload"])
def tests():
    subprocess.run(["nox", "-s", "tests"])


def fix():
    subprocess.run(["nox", "-s", "fix"])


def docs():
    subprocess.run(["nox", "-s", "docs"])
