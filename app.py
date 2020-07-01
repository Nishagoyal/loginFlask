from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
 
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"
    
@app.route("/salvador")
def about():
    return render_template("about.html")
@app.route("/index")
def index():
    return render_template("index.html")
@app.route("/temp")
def temp():
   return render_template("template.html")



@app.route('/login1', methods=['GET', 'POST'])
def login1():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login1.html', error=error)
    
if __name__ == "__main__":
    
   app.run(host='0.0.0.0', port=5000)
    