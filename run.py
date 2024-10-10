# from app import app, db
# from app.models import User, Feedback

# @app.shell_context_processor
# def make_shell_context():
#     return {'db': db, 'User': User, 'Feedback': Feedback}

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from models import User
from app.models import User

app = Flask(__name__)

# configs for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'  # will use SQLite for development at this point
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# then initialize the database
db = SQLAlchemy(app)

# then defining all my  models here (from users, feedback, and auth.)
# will init Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # The route name for login

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    app.run(debug=True)
