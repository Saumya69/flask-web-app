#standard routes of the website////blueprint allows to define routes in multiple files 
from flask import Flask, render_template
from flask import Blueprint
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)