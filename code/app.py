
# Flask tutorial http://flask.pocoo.org/docs/0.10/
# http://lesson-flask-124420.nitrousapp.com:5000/
# https://developer.mozilla.org/en-US/docs/Web/HTML

# Running the server from the console below
# $ cd
# $ . ./venv/bin/activate
# $ cd code
# $ python app.py
# Click Preview ^^ and click the "Port 5000" option

import json

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
#     query_params = request.args
    return 'goodbyet'

@app.route('/<name>')
def name(name):
    return render_template('index.html', text='howdy {name:s}'.format(name=name))

@app.route('/submission/', methods=['GET', 'POST'])
def submission():

    if request.method == 'GET':
        return render_template('submission_form.html')

    else:
        params = request.form.to_dict(flat=True)

        if params.get('name'):
            session['name'] = params.get('name')

        meta = {
            'method': request.method,
            'session': session
        }
        headers = "\n".join(["{:>30}  {:<20}".format(k, v) for k, v in request.headers.iteritems()])
        print headers

        return render_template('data.html', params=json.dumps(params, indent=2), meta=meta, headers=headers)

@app.route('/get-submission/', methods=['GET'])
def get_submission():

    params = request.form.to_dict(flat=True)

    if params.get('name'):
        session['name'] = params.get('name')

    meta = {
        'method': request.method,
        'session': session
    }
    headers = "\n".join(["{:>30} {:<20}".format(k, v) for k, v in request.headers.iteritems()])
    print headers

    return render_template('data.html', params=json.dumps(params, indent=2), meta=meta, headers=headers)

@app.route('/interactive/', methods=['GET', 'POST'])
def interactive():

    if request.method == 'GET':
        return render_template('interactive_form.html')

    else:
        params = request.form.to_dict(flat=True)

        if params.get('name'):
            session['name'] = params.get('name')

        meta = {
            'method': request.method,
            'session': str(session)
#             'session': session
        }
        headers = "\n".join(["{:>30}  {:<20}".format(k, v) for k, v in request.headers.iteritems()])
        print headers

        return json.dumps({"params": params, "meta": meta, "headers": headers}, indent=2)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, use_reloader=True, use_debugger=app.config['DEBUG'])
