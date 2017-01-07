
from flask_security import UserMixin, RoleMixin

from app import db

class Feedback(db.Model):
	"""  Model to store feedbak data """

	id = db.Column(db.Integer,primary_key=True)
	email = db.Column(db.String(100),index=True)
	feedback = db.Column(db.Text())
	timestamp = db.Column(db.DateTime)
	def __repr__(self):
		return '<Email: %r , Feedback: %s , Timestamp: %r >' % (self.email,self.feedback,self.timestamp)

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))



class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users,
            backref=db.backref('users', lazy='dynamic'))

    def __str__(self):
        return "<username :%s , first_name :%s , last_name :%s , email :%s ,active :%s , roles :%s>"%(self.username,self.first_name,self.last_name,self.email,self.active,self.roles)
    def __repr__(self):
        return "<username :%s , first_name :%s , last_name :%s , email :%s , active :%s ,  roles :%s>"%(self.username,self.first_name,self.last_name,self.email,self.active,self.roles)




