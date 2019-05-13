from flask import Flask
from flask import render_template
from flask import request
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
import cgi
form = cgi.FieldStorage()

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

with open('/var/www/html/flaskapp/config/public_ip.txt', 'r') as file:
    public_ip = file.read().replace('\n', '')

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
    return auth0.authorize_redirect(redirect_uri='http://{}/callback'.format(public_ip), audience='https://dev-jv5aht4v.auth0.com/userinfo')

@app.route('/callback')
def callback_handling():
    # Handles response from token endpoint
    auth0.authorize_access_token()
    resp = auth0.get('userinfo')
    userinfo = resp.json()
    #populate info table
    email = userinfo['email']
    if verifyLogin(userinfo['email']):
        db_user_info = dict(getInfo(userinfo['email']).items())
        sid = db_user_info['student_id']
        courses = getEnrollment(sid)
        db_user_info['courses'] = courses
        transactions = getTransactionDetails(sid)
        db_user_info['transactions'] = transactions
    else:
        db_user_info = {'first_name': 'Unregistered', 'last_name': 'User'}

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

@app.route('/edit')
@requires_auth
def edit():
    return render_template('edit.html')

@app.route('/edit', methods=['POST'])
@requires_auth
def form():
    email = session['profile']['email']
    new_sec_email = ''
    new_address = ''
    new_phone = ''
    new_sec_email = request.form['sec_email']
    if new_sec_email is not '':
        UpdateSecondaryEmail(email, new_sec_email)
        session['webUserInfo']['sec_email'] = new_sec_email
        session.modified = True
    new_address = request.form['address']
    if new_address is not '':
        UpdateAddress(email, new_address)
        session['webUserInfo']['address'] = new_address
        session.modified = True
    new_phone = request.form['phone']
    if new_phone is not '':
        UpdatePhone(email, new_phone)
        session['webUserInfo']['phone'] = new_phone
        session.modified = True
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    # Clear session stored data
    session.clear()
    # Redirect user to logout endpoint
    params = {'returnTo': 'http://{}/'.format(public_ip), 'client_id': 'Wjqx-VAEe4AbTBHtScwLn-QCvpxewOe9'}
    return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))

if __name__ == '__main__':
  app.run(debug=True)
