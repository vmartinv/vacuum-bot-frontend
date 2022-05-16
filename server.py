from flask import Flask, render_template
from flask import request, send_from_directory
from flask_limiter import Limiter
import os.path

app = Flask(__name__)

limiter = Limiter(
    app,
    key_func=lambda: 'global',
    default_limits=["200 per day", "50 per hour"]
)

VALID_DIRECTIONS = ["forward", "right", "back", "left"]

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static', 'img'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/site.webmanifest')
def site_webmanifest():
   return send_from_directory(os.path.join(app.root_path, 'static'),
                              'site.webmanifest', mimetype='application/manifest+json')

@app.route('/')
@limiter.limit("20 per minute")
def index():
    return render_template('index.html')

@app.route('/move_robot', methods = ['POST'])
@limiter.limit("600 per minute")
def move_robot():
    direction = request.form.get('direction', "")
    if direction not in VALID_DIRECTIONS:
        abort(400, 'Invalid direction')
    response = call_service(direction)
    if response.status_code != 200:
        print(response)
        print(response.text)
        abort(500, 'Service failure')
    return direction
