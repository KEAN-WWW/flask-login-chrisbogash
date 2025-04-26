from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from flask_login import login_user, logout_user
from application.bp.authentication.forms import RegisterForm, LoginForm
from application.bp.homepage import homepage
from application.database import User, db

authentication = Blueprint('authentication', __name__, template_folder='templates')

@authentication.route('/registration', methods=['POST', 'GET'])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        user_check = User.find_user_by_email(form.email.data)
        if user_check is None:
            user = User.create(form.email.data, form.password.data)
            user.save()
            return redirect(url_for("authentication.dashboard", name="dash"))
        else:
            flash("Already Registered!")
    return render_template('registration.html', form=form)
    pass


@authentication.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.find_user_by_email(form.email.data)
        if not user:
            flash('User Not Found')
            return redirect(url_for('authentication.login'))
        if not user.check_password(form.password.data):
            flash('Password Incorrect!')
            return redirect(url_for('authentication.login'))
        login_user(user)
        flash('Login Successful!')
        return redirect(url_for('authentication.dashboard'))
    return render_template('login.html', form=form)
    pass

@authentication.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@authentication.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('homepage.homepage'))