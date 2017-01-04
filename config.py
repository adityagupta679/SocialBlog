import os

basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = "Hard to Guess"

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'foo.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
