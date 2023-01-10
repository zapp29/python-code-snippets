from flask import Flask, request, url_for, render_template, make_response, redirect
from markupsafe import escape
from werkzeug.utils import secure_filename

app = Flask(__name__)

"""
TODO:
- [ ] Add a route for /upload that accepts POST requests and saves the file to the uploads folder
- [ ] Add menu with hyperlinks to all routes in the index page
"""

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
