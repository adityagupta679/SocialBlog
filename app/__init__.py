from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
from flask_security.utils  import encrypt_password


app=Flask(__name__)
app.config.from_object('config')



from flask_bootstrap import Bootstrap

bootstrap= Bootstrap(app)
db=SQLAlchemy(app)

from app import views,errors,models

# import user and role models 
from models import User,Role


# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

@app.before_first_request
def before_first_request():
	# create database and a test user
    try:
    	models.db.drop_all()
        models.db.create_all()
        user_datastore.create_user(username='test_user1',email='test_user1@test.com', password=encrypt_password('password'))
        db.session.commit()
        print ("Database Created")
    except Exception, e:
        app.logger.error(str(e))