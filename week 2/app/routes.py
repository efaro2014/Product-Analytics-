from app import application
from flask import render_template 


@application.route('/')

def index():
	return ('<h1> Hello World </h1>')