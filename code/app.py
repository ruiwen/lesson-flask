
from flask import Flask
from flask import request
from flask import session
from flask import url_for
from flask import render_template

DEBUG = True
SECRET_KEY = 'thisismysupersecretkey'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    return 'hello world woot woot'

@app.route('/<name>')
def name(name):
    return 'hello {name:s}'.format(name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, use_reloader=True, use_debugger=app.config['DEBUG'])
