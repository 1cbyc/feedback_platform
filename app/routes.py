from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, logout_user, login_required, current_user
from app import app, db
# from models import User
# from forms import RegistrationForm, LoginForm
from app.forms import RegistrationForm, FeedbackForm
from app.models import User, Feedback

@app.route('/')
def home():
    return render_template('base.html')

# for the register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        # user = User(username=form.username.data, email=form.email.data, password_hash=form.password.data)
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        # flash('Your account has been created!', 'success')
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
        # return redirect(url_for('home'))
        
    return render_template('register.html', form=form)

# for the login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login successful!')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password.')
    
    return render_template('login.html', form=form)

# for logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('index'))

# @app.route('/feedback', methods=['GET', 'POST'])
# @login_required
# def feedback():
#     form = FeedbackForm()
#     if form.validate_on_submit():
#         feedback = Feedback(user_id=current_user.id, feedback_text=form.feedback_text.data)
#         db.session.add(feedback)
#         db.session.commit()
#         flash('Your feedback has been submitted!', 'success')
#         return redirect(url_for('home'))
#     return render_template('feedback_form.html', form=form)

# @app.route('/dashboard')
# @login_required
# def dashboard():
#     feedbacks = Feedback.query.filter_by(user_id=current_user.id).all()
#     return render_template('dashboard.html', feedbacks=feedbacks)

# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('home'))

# will add other routes for login and any additional features here
