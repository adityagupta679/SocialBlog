from app import app
from flask import render_template
from .forms import FeedBackForm



@app.route('/')
@app.route('/index')
def index():
	params={}
	params["Name"]="Aadi"
	params["title"]="Hello"
	return render_template('index.html',params=params)
	# return "Hello Developer",302

@app.route('/feedback',methods=['GET','POST'])
def feedback():
	params={}
	params["Name"]="Aadi"
	params["title"]="Feedback"
	form=FeedBackForm()
	return render_template('feedback.html',params=params,form=form)
