from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
auth = Blueprint('auth', __name__) # Create blueprint
from flask_login import login_user, login_required, logout_user, current_user
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': # check
        email = request.form.get('email') # Get form data
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first() # Check if user exists in database
        if user:
            if check_password_hash(user.password, password):
                flash('You have Logged in succesfully', category='success')
                login_user(user, remember=True) # Log user in
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user = current_user)

@auth.route('/logout')
@login_required # Decorator which checks if user is logged in
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    
    if request.method == 'POST': # check
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # Add user to database
            new_user = User(
                            email=email,
                            first_name=first_name,
                            password=generate_password_hash(password1, method='sha256')
                            )
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("signup.html", user = current_user)