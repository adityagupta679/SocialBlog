from flask import Flask

app=Flask(__name__)

from app import views,errors

from flask_bootstrap import Bootstrap

bootstrap= Bootstrap(app)
