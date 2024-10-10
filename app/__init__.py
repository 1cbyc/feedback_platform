from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # using sqlite for simplicity at this point
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # will redirect to login page once the user is not authenticated

from app import routes # then import the routes at the end to avoid circular imports
