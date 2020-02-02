from flask import Flask,render_template,redirect,url_for
from forms import *
import os
app = Flask(__name__)
app.secret_key=os.environ.get('SECRET')
app.config['SECRET_KEY']= 'mysecret'

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/login',methods=['GET', 'POST', 'PUT'])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        return redirect(url_for('welcome'))
    return  render_template('login.html',loginForm=loginForm)

@app.route('/register',methods=['GET', 'POST', 'PUT'])
def register():
    regisForm =RegisterForm()
    if regisForm.validate_on_submit():
        return redirect(url_for('login'))
    return  render_template('register.html',regisForm=regisForm)

@app.route('/welcome')
def welcome():
    return "welcome"




if __name__ == '__main__':
    app.run(debug=True)