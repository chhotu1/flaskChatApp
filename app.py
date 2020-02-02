from flask import Flask,render_template
import os
app = Flask(__name__)
app.secret_key=os.environ.get('SECRET')
app.config['SECRET_KEY']= 'mysecret'

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)