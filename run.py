from app import app, db
from app.models import User, Feedback

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Feedback': Feedback}

if __name__ == '__main__':
    app.run(debug=True)
    

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# configs for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'  # will use SQLite for development at this point
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# then initialize the database
db = SQLAlchemy(app)

# Define your models here (User, Feedback, etc.)

if __name__ == '__main__':
    app.run(debug=True)

