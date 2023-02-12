import os

from flask import Flask, request, url_for, render_template, make_response, redirect, session, flash, get_flashed_messages
from markupsafe import escape
from werkzeug.utils import secure_filename

from .db import db

"""
TODO:
- [ ] Add a route for /upload that accepts POST requests and saves the file to the uploads folder
- [ ] Add menu with hyperlinks to all routes in the index page
- [ ] Check what the pin is for
- [ ] Check how the global objects request and session are handled by flask
"""


def config_app(test_config, app):
    app.config.from_mapping(
        SECRET_KEY='dev', # FOR DEV USE ONLY; change this in production for 'secrets.token_hex()' or set SECRET_KEY in config.py
        DATABASE=os.path.join(app.instance_path, 'simple_flask_rest_api.sqlite'),
    )
    if test_config is None:
        # load the PROD config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
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

    # use app.get() for GET requests
    @app.get('/')
    def index():
        return render_template('index.html')

    # use methods parameter to specify which HTTP methods are allowed
    @app.route('/methods', methods=['GET', 'POST'])
    def methods():
        return request.method

    @app.route('/variables/<var>')
    def variables(var):
        # using variables in a URL
        return f'Variable {escape(var)}'

    @app.route('/path/<path:subpath>')
    def subpath(subpath):
        # Using variables with type converters: string, int, float, path, uuid
        # show the subpath after /path/
        return f'Subpath {escape(subpath)}'

    @app.route('/urls')
    def show_urls():
        # show urls for different assets
        urls = url_for('index') + '<br>' + \
               url_for('methods') + '<br>' + \
               url_for('variables', username='John Doe') + '<br>' + \
               url_for('subpath', subpath='some_path') + '<br>' + \
               url_for('static', filename='style.css')
        return urls

    @app.route('/template/')
    @app.route('/template/<name>')
    def template(name="World"):
        return render_template('template.html', name=name)

    @app.route('/show_request')
    def show_request():
        # show the request proxy object
        return \
            f"<b>method</b>: {request.method}<br>" \
            f"<b>url</b>: {request.url}<br>" \
            f"<b>headers</b>: {request.headers}<br>" \
            f"<b>args</b>: {request.args}<br>" \
            f"<b>form</b>: {request.form}<br>" \
            f"<b>data</b>: {request.data}<br>" \
            f"<b>files</b>: {request.files}<br>"

    @app.route('/upload', methods=['GET', 'POST'])
    def upload_file():
        if request.method == 'POST':
            file = request.files['the_file']
            file.save(f'/var/www/uploads/{secure_filename(file.filename)}')
            return f'upload file: {request.files}'
        else:
            return '''
                <!doctype html>
                <title>Upload new File</title>
                <h1>Upload new File</h1>
                <form method=post enctype=multipart/form-data>
                <input type=file name=file>
                <input type=submit value=Upload>
                </form>'''

    @app.route('/set_cookie', methods=['GET'])
    def set_cookie():
        # set cookie
        response = make_response('set cookie')
        response.set_cookie('answer', '43')
        return response

    @app.route('/get_cookie', methods=['GET'])
    def get_cookie():
        # get cookie
        return request.cookies.get('answer')

    @app.route('/redirect')
    def redirect_():
        return redirect(url_for('index'))

    @app.errorhandler(404)
    def page_not_found(error):
        response = error.get_response()
        response_elements = [
            (el, eval('response.' + el, {'response': response}))
            for el in dir(response) if not el.startswith('_')
        ]
        return render_template(
            'page_not_found.html',
            response_elements=response_elements,
        ), 404

    import secrets
    app.secret_key = secrets.token_hex()

    @app.route('/sessions')
    def sessions():
        if 'username' in session:
            return f'Logged in as {session["username"]}. <br>' \
                   f'Session cookie: {request.cookies.get("session")} <br>' \
                   f'<a href="/sessions/logout">Logout</a>'
        return 'You are not logged in. <a href="/sessions/login">Login</a>'

    @app.route('/sessions/login', methods=['GET', 'POST'])
    def sessions_login():
        if request.method == 'POST':
            session['username'] = request.form['username']
            return redirect(url_for('sessions'))
        return '''
            <form method="post">
                <p><input type=text name=username>
                <p><input type=submit value=Login>
            </form>
        '''

    @app.route('/sessions/logout')
    def sessions_logout():
        # remove the username from the session if it's there
        session.pop('username', None)
        return redirect(url_for('sessions'))

    @app.route('/flash')
    def flash_message():
        import random
        random_message = ''.join(random.choices(["a", "b", "c", "d", "e"], k=5))
        message_category = random.choice(['message', 'info', 'warning', 'error'])
        flash(random_message, message_category)
        return redirect(url_for('index'))

    @app.route('/show_flashed')
    def show_flashed_message():
        return get_flashed_messages(with_categories=True)

    db.init_app(app)



    return app
