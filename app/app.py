from flask import (Blueprint, render_template, request,
                   redirect, flash, url_for, g, current_app)
from flask_login import (login_user, logout_user, current_user, login_required)

from . import db
from .models import User
from .utils import validate_captcha

main = Blueprint('main', __name__)


@main.before_app_request
def before_request():
    g.user = current_user


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    """The main page for the app"""
    return render_template('index.html')


@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    if current_app.config.get('SHOW_CAPTCHA'):
        captcha_response = request.form.get('g-recaptcha-response')
        if not validate_captcha(captcha_response):
            flash('Bad Captcha')
            return redirect(url_for('main.register'))

    email = request.form['email']
    password = request.form['password']
    password_confirm = request.form['password_confirm']

    if password != password_confirm:
        flash('Passwords must match!')
        return redirect(url_for('main.register'))

    user = User.create(email, password)

    try:
        db.session.add(user)
        db.session.commit()
    except:
        flash('User already exists!')
        return redirect(url_for('main.register'))

    return redirect(url_for('main.login'))


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form['email']
    password = request.form['password']

    if current_app.config.get('SHOW_CAPTCHA'):
        captcha_response = request.form.get('g-recaptcha-response')
        if not validate_captcha(captcha_response):
            flash('Bad Captcha')
            return redirect(url_for('main.login'))

    registered_user = User.get_user(username, password)

    if registered_user is None:
        flash('Username or Password is invalid')
        return redirect(url_for('main.login'))
    else:
        login_user(registered_user)

    flash('Logged in successfully')
    return redirect(url_for('main.index'))


@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
