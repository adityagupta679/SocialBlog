from app import app
from flask import render_template,redirect,flash,url_for
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
	form=FeedBackForm()

	params={}
	params["Name"]="Aadi"
	params["title"]="Feedback"
	if form.validate_on_submit():
		flash("Feedback received. We will get back to you at %s"%(form.email.data))
		return redirect(url_for('index'))
	return render_template('feedback.html',params=params,form=form)
