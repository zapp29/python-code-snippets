from flask import (
    Blueprint,
    get_flashed_messages,
    make_response,
    render_template,
    session, current_app,
)
from markupsafe import escape

index_blueprint = Blueprint("index", __name__, url_prefix="/")


# use app.get() for GET requests
@index_blueprint.get("/")
def index():
    return render_template("index.html")


# use methods parameter to specify which HTTP methods are allowed
@index_blueprint.route("/methods", methods=["GET", "POST"])
def methods():
    return request.method


@index_blueprint.route("/variables/<var>")
def variables(var):
    # using variables in a URL
    return f"Variable {escape(var)}"


@index_blueprint.route("/path/<path:subpath>")
def subpath(subpath):
    # Using variables with type converters: string, int, float, path, uuid
    # show the subpath after /path/
    return f"Subpath {escape(subpath)}"


@index_blueprint.route("/urls")
def show_urls():
    # show urls for different assets
    urls = (
        url_for("index.index")
        + "<br>"
        + url_for("index.methods")
        + "<br>"
        + url_for("index.variables", var="John Doe")
        + "<br>"
        + url_for("index.subpath", subpath="some_path")
        + "<br>"
        + url_for("static", filename="style.css")
    )
    return urls


@index_blueprint.route("/template/")
@index_blueprint.route("/template/<name>")
def template(name="World"):
    return render_template("template.html", name=name)


@index_blueprint.route("/show_request")
def show_request():
    # show the request proxy object
    return (
        f"<b>method</b>: {request.method}<br>"
        f"<b>url</b>: {request.url}<br>"
        f"<b>headers</b>: {request.headers}<br>"
        f"<b>args</b>: {request.args}<br>"
        f"<b>form</b>: {request.form}<br>"
        f"<b>data</b>: {request.data}<br>"
        f"<b>files</b>: {request.files}<br>"
    )

import os
from flask import flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


@index_blueprint.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index.download_file', name=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@index_blueprint.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(current_app.config["UPLOAD_FOLDER"], name)


@index_blueprint.route("/set_cookie", methods=["GET"])
def set_cookie():
    # set cookie
    response = make_response("set cookie")
    response.set_cookie("answer", "43")
    return response


@index_blueprint.route("/get_cookie", methods=["GET"])
def get_cookie():
    # get cookie
    return request.cookies.get("answer")


@index_blueprint.route("/redirect")
def redirect_():
    return redirect(url_for("index.index"))


@index_blueprint.errorhandler(404)
def page_not_found(error):
    response = error.get_response()
    response_elements = [
        (el, eval("response." + el, {"response": response}))
        for el in dir(response)
        if not el.startswith("_")
    ]
    return (
        render_template(
            "page_not_found.html",
            response_elements=response_elements,
        ),
        404,
    )


import secrets

index.secret_key = secrets.token_hex()


@index_blueprint.route("/sessions")
def sessions():
    if "username" in session:
        return (
            f'Logged in as {session["username"]}. <br>'
            f'Session cookie: {request.cookies.get("session")} <br>'
            f'<a href="/sessions/logout">Logout</a>'
        )
    return 'You are not logged in. <a href="/sessions/login">Login</a>'


@index_blueprint.route("/sessions/login", methods=["GET", "POST"])
def sessions_login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect(url_for("index.sessions"))
    return """
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    """


@index_blueprint.route("/sessions/logout")
def sessions_logout():
    # remove the username from the session if it's there
    session.pop("username", None)
    return redirect(url_for("index.sessions"))


@index_blueprint.route("/flash")
def flash_message():
    import random

    random_message = "".join(random.choices(["a", "b", "c", "d", "e"], k=5))
    message_category = random.choice(["message", "info", "warning", "error"])
    flash(random_message, message_category)
    return redirect(url_for("index.index"))


@index_blueprint.route("/show_flashed")
def show_flashed_message():
    return get_flashed_messages(with_categories=True)


from functools import wraps
from flask import g, request, redirect, url_for


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("username") is None:
            return redirect(url_for('index.sessions_login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@index_blueprint.route('/logged_in_only')
@login_required
def logged_in_only():
    return "this is for logged in only"

