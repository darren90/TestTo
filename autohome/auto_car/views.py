
from models import *
from datetime import datetime
from  flask import Flask,render_template,request,jsonify

from app import app

@app.route('/view')
def myindex():
    return "Hello da feige -hahhah"#render_template("index.html",todos=todos,form=form)


@app.route('/')
def index():
    return  render_template("index_1.html")




@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')