from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, validators
# from wtforms.validators import Required,Email

class FeedBackForm(FlaskForm):
	"""FeedbackForm Class"""
	email = StringField('Email',[validators.DataRequired(message="Please enter email"),validators.Email(message= "Email address is not valid.")])
	feedback = TextAreaField('Enter Your Feedback',[validators.DataRequired(message="Feedback is required")])
	submit = SubmitField('Submit')
