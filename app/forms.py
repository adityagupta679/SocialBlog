from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required,Email

class FeedBackForm(FlaskForm):
	"""FeedbackForm Class"""
	email=StringField('email',validators=[Required(),Email()])
	feedback= TextAreaField('Enter Your Feedback',validators=[Required()],default="Great Work !! I look forward to using this site for all my Social Blogging needs.")
	submit=SubmitField('Submit')
