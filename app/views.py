from app import app,db,models
from flask import render_template,redirect,flash,url_for
from .forms import FeedBackForm

from flask_security import login_required
from models import Feedback,User,Role

import datetime

@app.route('/')
@app.route('/index')
def index():
	params={}
	params["Name"]="Aadi"
	params["title"]="Hello"
	return render_template('index.html',params=params)
	# return "Hello Developer",302


# Feedback form view

@app.route('/feedback',methods=['GET','POST'])
def feedback():
	form=FeedBackForm()

	params={}
	params["Name"]="Aadi"
	params["title"]="Feedback"
	if form.validate_on_submit():

		# saving form data to a database table
		feedback = Feedback(email = form.data['email'],feedback = form.data['feedback'], timestamp=datetime.datetime.utcnow())
		try:
			db.session.add(feedback)
			db.session.commit()
		except Exception, e:
			# handle the exception in case insertion into database doesnt work , and log the error
			db.session.rollback()
			flash("Feedback failed due to some error. Please try again.")
			app.logger.error(str(e))
			return render_template('feedback.html',params=params,form=form)


		flash("Feedback received. We will get back to you at %s ASAP"%(form.email.data))
		return redirect(url_for('index'))
	return render_template('feedback.html',params=params,form=form)

# admin route to see the feedbacks Auth Required

@app.route('/admin/feedbacks')
@login_required
def display_feedbacks():
	params={}
	params["Name"]="Aadi"
	params["title"]="Feedbacks Received"
	feedbacks=models.Feedback.query.order_by('timestamp desc').all()
	return render_template('admin/feedback_display.html',feedbacks = feedbacks,params = params)


	