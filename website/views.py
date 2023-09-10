#standard routes of the website////blueprint allows to define routes in multiple files 
from flask import Flask, render_template
from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")