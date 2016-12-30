from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	params={}
	params["Name"]="Aadi"
	params["title"]="Hello"
	return render_template('index.html',params=params)
	# return "Hello Developer",302


