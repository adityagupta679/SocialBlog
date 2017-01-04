
from app import db

class Feedback(db.Model):
	"""  Model to store feedbak data """

	id = db.Column(db.Integer,primary_key=True)
	email = db.Column(db.String(100),index=True)
	feedback = db.Column(db.Text())

	def __repr__(self):
		return '<Email: %r , /n Feedback: %s >' % (self.email,self.feedback)


