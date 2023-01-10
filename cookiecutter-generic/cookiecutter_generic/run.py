import subprocess
import sys


def from_config(args=None):
    if args is None:
        args = sys.argv[1:]
    for arg in args:
        print(f"Running configuration file: {arg}")
        subprocess.run(
            ['cookiecutter', '.', '--config-file', arg]
        )
    else:
        print(f"Finished running configuration files: {args}")
