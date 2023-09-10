#standard routes of the website////blueprint allows to define routes in multiple files 
from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1> Hello </h1>"