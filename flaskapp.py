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
import requests
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

with open('/var/www/html/flaskapp/config/url.txt', 'r') as file:
    url = file.read().replace('\n', '')

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
    return auth0.authorize_redirect(redirect_uri='http://{}/callback'.format(url), audience='https://dev-jv5aht4v.auth0.com/userinfo')

@app.route('/callback')
def callback_handling():
    # Handles response from token endpoint
    auth0.authorize_access_token()
    session.clear()
    resp = auth0.get('userinfo')
    userinfo = resp.json()
    #populate info table
    email = userinfo['email']
    if verifyRole(email) is 'student':
        db_user_info = dict(getInfo(email).items())
        sid = db_user_info['student_id']
        courses = getEnrollment(sid)
        db_user_info['courses'] = courses
        transactions = getTransactionDetails(sid)
        db_user_info['transactions'] = transactions
    elif verifyRole(email) is 'teacher':
        db_user_info = dict(getTeacherInfo(email).items())
    else:
        db_user_info = {'first_name': 'Unregistered', 'last_name': 'User'}

    session['webUserInfo'] = db_user_info
    session['profile'] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture'],
        'email': email
    }
    return redirect('/loggedin')

@app.route('/loggedin')
@requires_auth
def loggedin():
    return render_template('loggedin.html', userinfo=session['profile'], dbuserinfo=session['webUserInfo'])

@app.route('/dashboard')
@requires_auth
def dashboard():
    sjsu_weather = 'https://api.darksky.net/forecast/31571daf618cff5e698e9e539077ab18/37.3357807,-121.8821639'
    r = requests.get(url = sjsu_weather)
    weather = r.json()
    session['webUserInfo']['weather'] = weather
    sjsu_news = 'https://newsapi.org/v2/everything?q=+SJSU&language=en&sortby=relevancy&apiKey=c10d5c779e324c6ebf5302c19f254771'
    r = requests.get(url = sjsu_news)
    news = r.json()
    session['webUserInfo']['news'] = news
    session.modified = True
    return render_template('dashboard.html', userinfo=session['profile'], dbuserinfo=session['webUserInfo'], weather=session['webUserInfo']['weather'], news=session['webUserInfo']['news'])

@app.route('/dashboard_teacher')
@requires_auth
def dashboard_teacher():
    sjsu_weather = 'https://api.darksky.net/forecast/31571daf618cff5e698e9e539077ab18/37.3357807,-121.8821639'
    r = requests.get(url = sjsu_weather)
    weather = r.json()
    session['webUserInfo']['weather'] = weather
    sjsu_news = 'https://newsapi.org/v2/everything?q=+SJSU&language=en&sortby=relevancy&apiKey=c10d5c779e324c6ebf5302c19f254771'
    r = requests.get(url = sjsu_news)
    news = r.json()
    session['webUserInfo']['news'] = news
    session.modified = True
    return render_template('dashboard_teacher.html', userinfo=session['profile'], dbuserinfo=session['webUserInfo'], weather=session['webUserInfo']['weather'], news=session['webUserInfo']['news'])

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
    params = {'returnTo': 'http://{}/'.format(url), 'client_id': 'Wjqx-VAEe4AbTBHtScwLn-QCvpxewOe9'}
    return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))

if __name__ == '__main__':
  app.run(debug=True)
