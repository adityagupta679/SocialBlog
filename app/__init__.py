from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config.from_object('config')


from flask_bootstrap import Bootstrap

bootstrap= Bootstrap(app)
db=SQLAlchemy(app)

from app import views,errors,models

@app.before_first_request
def before_first_request():
    try:
        models.db.create_all()
        db.session.commit()
        print ("Database Created")
    except Exception, e:
        app.logger.error(str(e))