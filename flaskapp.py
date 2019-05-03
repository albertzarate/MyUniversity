from flask import Flask
from flask import render_template
from functools import wraps
import json
from os import environ as env
from werkzeug.exceptions import HTTPException
from flask import jsonify
from flask import redirect
from flask import session
from flask import url_for
from authlib.flask.client import OAuth
from six.moves.urllib.parse import urlencode
from functools import wraps
from sql import *

app = Flask(__name__)
app.secret_key = "MPiVP8ZtlTBI7h_7V6FJZf8gfopHOMoDSjtTIz0fLZMPWeYxYYH6cYfKW0tJgPeW"
oauth = OAuth(app)

auth0 = oauth.register(
    'auth0',
    client_id='Wjqx-VAEe4AbTBHtScwLn-QCvpxewOe9',
    client_secret='MPiVP8ZtlTBI7h_7V6FJZf8gfopHOMoDSjtTIz0fLZMPWeYxYYH6cYfKW0tJgPeW',
    api_base_url='https://dev-jv5aht4v.auth0.com',
    access_token_url='https://dev-jv5aht4v.auth0.com/oauth/token',
    authorize_url='https://dev-jv5aht4v.auth0.com/authorize',
    client_kwargs={
        'scope': 'openid email profile',
    },
)

def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    if 'profile' not in session:
      # Redirect to Login page here
      return redirect('/')
    return f(*args, **kwargs)

  return decorated

@app.route('/')
def hello_world():
  return render_template("index.html")

@app.route('/login')
def login():
    return auth0.authorize_redirect(redirect_uri='http://18.222.192.36/callback', audience='https://dev-jv5aht4v.auth0.com/userinfo')

@app.route('/callback')
def callback_handling():
    # Handles response from token endpoint
    auth0.authorize_access_token()
    resp = auth0.get('userinfo')
    userinfo = resp.json()
    #populate info table
    if verifyLogin(userinfo['email']):
        db_user_info = dict(getInfo(userinfo['email']).items())
        courses = getEnrollment(db_user_info['student_id'])
        db_user_info['courses'] = courses
    else:
        db_user_info = {'first_name': 'Unregistered', 'last_name': 'User'}
        courses = ['N/A']

    session['webUserInfo'] = db_user_info
    session['profile'] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture'],
        'email': userinfo['email']
    }
    return redirect('/loggedin')

@app.route('/loggedin')
@requires_auth
def loggedin():
    return render_template('loggedin.html', userinfo=session['profile'], dbuserinfo=session['webUserInfo'])

@app.route('/dashboard')
@requires_auth
def dashboard():
    return render_template('dashboard.html', userinfo=session['profile'], dbuserinfo=session['webUserInfo'])

@app.route('/logout')
def logout():
    # Clear session stored data
    session.clear()
    # Redirect user to logout endpoint
    params = {'returnTo': 'http://18.222.192.36/', 'client_id': 'Wjqx-VAEe4AbTBHtScwLn-QCvpxewOe9'}
    return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))

if __name__ == '__main__':
  app.run(debug=True)
