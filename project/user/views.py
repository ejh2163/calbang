from flask import Flask, flash, request, render_template, redirect, session, url_for, Blueprint
from models import User

from flask_login import login_required, login_user, current_user, logout_user, confirm_login, login_fresh
from .user_forms import LoginForm, RegisterForm


user_blueprint = Blueprint('user', __name__, template_folder='templates')


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash('You are already logged in')
        return redirect(url_for('home'))
    
    form = RegisterForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            if User.is_email_taken(form.email.data):
                flash('This email is already registered!')
            elif User.is_username_taken(form.username.data):
                flash('This username is already taken!')
            else:    
                new_user = User(
                    date_joined = strftime("%Y-%m-%d"),
                    email = form.email.data,
                    username = form.username.data,
                    password = form.password.data,
                    verified = 0
                    )
                db.session.add(new_user)
                db.session.commit()
                
                # commented until email verification is set up: return redirect(url_for('verify'))
                flash('You have succesfully been registered!')
                return redirect(url_for('home'))
                
            return render_template('/register.html', form=form)
        else:
            return render_template('/register.html', form=form)
    elif request.method == 'GET':
        return render_template('/register.html', form=form)

@user_blueprint.route('/verify')
def verify():
    return render_template('/verify.html')

@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already logged in')
        return redirect(url_for('home'))
    
    form = LoginForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            user, authenticated = User.authenticate(form.username.data, form.password.data)
            if user:
                if authenticated:
                    login_user(user, remember=form.remember_me.data)
                    flash('You have successfully logged in')
                    return redirect(url_for('home'))
                else:
                    flash('아이디/비밀번호가 일치하지 않습니다')
                    return render_template('/login.html', form=form)
            else:
                flash('아이디가 가입되지 않았습니다')
                return render_template('/login.html', form=form)
        else:
            return render_template('/login.html', form=form)
    elif request.method == 'GET':
        return render_template('/login.html', form=form)

@user_blueprint.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    logout_user()
    return redirect(url_for('home'))

@user_blueprint.route('/profile')
@login_required
def profile():
    return render_template('/profile.html')

