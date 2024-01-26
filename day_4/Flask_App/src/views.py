from flask import render_template, request, redirect, url_for, flash, Blueprint
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import login_user, logout_user, login_required, current_user
from .database import *

# create a blueprint for the views
views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@views.route('/home', methods=['GET', 'POST'])
def home():
    if current_user.is_authenticated:
        return redirect(url_for('views.dashboard'))
    return render_template('home.html')


@views.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', current_user=current_user)


# Create a login form
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Login')



@views.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = get_user_by_email(form.email.data)
            if user:
                if user.check_password(form.password.data):
                    login_user(user, remember=True)
                    flash('Login successful', category='success')
                    return redirect(url_for('views.dashboard'))
                else:
                    flash('Incorrect password, try again', category='error')
            else:
                flash('Email does not exist', category='error')
    return render_template('login.html', form=form)


# Create a registration form
class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password1 = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField('Create Account')

    # Custom validator
    def validate_email(self, email):
        '''Check if email already exists'''
        user = get_user_by_email(email = email.data)
        if user:
            raise ValidationError('Email already exists')



@views.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_user = create_user(name = form.username.data, email = form.email.data, password = form.password1.data)
            login_user(new_user, remember=True)
            flash('Account created!')
            return redirect(url_for('views.dashboard'))
        else:
            flash(f"Invalid input { form.errors }")
    return render_template('register.html', form=form)


@views.route('/logout')
@login_required
def logout():
    logout_user() # logout the user curtesy of flask_login
    return redirect(url_for('views.home'))


# Python package search on pypi.org
