from flask import Flask,render_template, redirect,url_for,request,session,flash
from datetime import datetime
import sys

app=Flask(__name__)
app.config['SECRET_KEY']='1234'   

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('login.html')

if __name__ == '__main__':
	app.run(debug = True)