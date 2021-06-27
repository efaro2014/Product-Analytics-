from app import application
from flask import render_template, redirect, url_for 
from flask_wtf import FlaskForm 
from wtforms import StringField
from flask_wtf.file import FileField, FileRequired, DataRequired
from wtforms import SubmitField 
import os 

class UploadFileFrom(FlaskForm):
	'Class for uploading a file when submitted'
	file_selector = FileField('File', validators=[FileRequired()])
	submit = SubmitField('Submit')

@application.route('/index')
@application.route('/')
def index():
	return (render_template('index.html', author='Diane Woodbridge'))

@application.route('/upload', methods=['GET', 'POST'])
def upload():
	file = UploadFileFrom()
	# if the file is validated grab the data
	if file.validate_on_submit():
		f = file.file_selector.data
		filename = f.filename

		# store the file in temporary directory 
		file_dir_path = os.path.join(application.instance_path, 'files')
		# connect the dir with the file 
		file_path = os.path.join(file_dir_path, filename)
		f.save(file_path)

		return redirect(url_for('index')) # call the index function to render the html 

	return render_template('upload.html', form=file)


class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

@application.route('/submit', methods=['GET', 'POST'])
def submit():
 	form = MyForm()
 	if form.validate_on_submit():
 		return redirect(url_for('/index'))
 	return render_template('upload.html', form=form)










