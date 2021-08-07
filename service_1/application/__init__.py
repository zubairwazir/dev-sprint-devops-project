from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import routes 

app = Flask(__name__)

app.config.update(
    SQLALCHEMY_DTATABASE_URI = 'sqlite:///data.db',
    SQLALCHEMY_TRACK_MODIFICATIONS = True,
    SECRET_KEY = 'password'

)

db = SQLAlchemy(app)
