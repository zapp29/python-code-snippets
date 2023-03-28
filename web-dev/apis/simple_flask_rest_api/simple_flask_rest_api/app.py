import os

from flask import Flask

"""
TODO:
- [ ] Add a route for /upload that accepts POST requests and saves the file to the uploads folder
- [ ] Add menu with hyperlinks to all routes in the index page
- [ ] Check what the pin is for
- [x] Check how the global objects request and session are handled by flask
- [ ] write basic documentation for the app
"""


def config_app(test_config, app):
    app.config.from_mapping(
        SECRET_KEY="dev",  # FOR DEV USE ONLY; change this in production for 'secrets.token_hex()' or set SECRET_KEY in config.py
        DATABASE=os.path.join(app.instance_path, "simple_flask_rest_api.sqlite"),
    )
    if test_config is None:
        # load the PROD config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    return app


def create_app(test_config=None):
    """
    This is the application factory function that creates and configures an instance of the Flask application.
    :param test_config: TODO
    :return: TODO
    """
    app = Flask(__name__, instance_relative_config=True)
    app = config_app(test_config, app)

    app.config['UPLOAD_FOLDER'] = '.'#'/var/www/uploads/'
    app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

    import db

    db.init_app(app)

    import views

    app.register_blueprint(views.index_blueprint)

    return app

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=5000)
