from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, validators
# from wtforms.validators import Required,Email

class FeedBackForm(FlaskForm):
	"""FeedbackForm Class"""
	email=StringField('Email',[validators.DataRequired(message="Please enter email"),validators.Email(message= "Email address is not valid.")])
	feedback= TextAreaField('Enter Your Feedback',[validators.DataRequired(message="Feedback is required")],default="Great Work !! I look forward to using this site for all my Social Blogging needs.")
	submit=SubmitField('Submit')
