from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import getenv
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Hillinger1993@35.242.176.52/flaskapp'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'jfdoifoidfdjfoijwdaspcvk0e9uwf8h8f' 

from application import routes

