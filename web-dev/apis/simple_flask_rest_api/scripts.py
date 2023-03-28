import argparse
import os


def tests():
    os.system("nox -R -s tests")


def fix():
    os.system("nox -R -s fix")


def docs():
    os.system("nox -R -s docs")


def app():
    os.system("flask --app simple_flask_rest_api run")


def debug():
    os.system("flask --app simple_flask_rest_api --debug run")


def init():
    os.system("flask --app simple_flask_rest_api init-db")


def deploy():
    """
    Function to deploy the Flask app to a production server.
    It builds a docker image, creates and run a container, and deploy the app to the cloud.
    :return:
    """
    parser = argparse.ArgumentParser(description='Utility script to deploy the Flask app to a production server.')
    parser.add_argument('platform', choices=['aws', 'gcloud', 'azure'], type=str, help='the platform to deploy to')
    args = parser.parse_args()
    os.system("poetry export -f requirements.txt --output simple_flask_rest_api/requirements.txt")
    os.system(f"docker build -t simple_flask_rest_api_{args.platform} -f Dockerfile_{args.platform} .")
