
from app import db

class Feedback(db.Model):
	"""  Model to store feedbak data """

	id = db.Column(db.Integer,primary_key=True)
	email = db.Column(db.String(100),index=True)
	feedback = db.Column(db.Text())
	timestamp = db.Column(db.DateTime)
	def __repr__(self):
		return '<Email: %r , Feedback: %s , Timestamp: %r >' % (self.email,self.feedback,self.timestamp)


