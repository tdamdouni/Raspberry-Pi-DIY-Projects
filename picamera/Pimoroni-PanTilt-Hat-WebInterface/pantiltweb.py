#!/usr/bin/env python
from sys import exit
from functools import wraps

try:
    import pantilthat
except ImportError:
    exit("This script requires the pantilthat module\nInstall with: sudo pip install pantilthat")

try:
    from flask import Flask, render_template, request, Response
    from flask_assets import Environment, Bundle
    from flask_ini import FlaskIni
except ImportError:
    exit("This script requires the flask module, flask_assets and flask_ini\nInstall with: sudo pip install Flask, sudo pip install Flask-ini and sudo pip install Flask-assets")

app = Flask(__name__)
assets = Environment(app)

app.iniconfig = FlaskIni()
with app.app_context():
    app.iniconfig.read('config.ini')

js = Bundle(
    'assets/jquery-3.2.1.js',
    filters='jsmin',
    output='gen/packed.js'
)
assets.register('js_all', js)

css = Bundle(
    'assets/bootstrap.min.css',
    'assets/bootstrap-theme.min.css',
    filters='cssmin',
    output='css/min.css'
)
assets.register('css_all', css)

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == app.iniconfig.get('user', 'name') and password == app.iniconfig.get('user', 'pass')

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/')
@requires_auth
def home(url=None):
    return render_template('webcam.html', url=app.iniconfig.get('webcam', 'url'))

@app.route('/api/<direction>/<int:angle>')
@requires_auth
def api(direction, angle):
    if angle < 0 or angle > 180:
        return "{'error':'out of range'}"

    angle -= 90

    if direction == 'pan':
        pantilthat.pan(angle)
        return '{{"direction": "pan", "angle":{}}}'.format(angle)

    elif direction == 'tilt':
        pantilthat.tilt(angle)
        return '{{"direction": "tilt", "angle":{}}}'.format(angle)

    return "{'error':'invalid direction'}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9595, debug=True)

