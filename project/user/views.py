from flask import Flask, flash, request, render_template, redirect, session, url_for, Blueprint
from project.models import User

from flask_login import login_required, login_user, current_user, logout_user, confirm_login, login_fresh
from .user_forms import LoginForm, RegisterForm

from project import db
from time import strftime

user_blueprint = Blueprint('user', __name__, template_folder='templates')


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    page='register'
    if current_user.is_authenticated:
        flash('이미 로그인된 상태입니다.')
        return redirect(url_for('home.home'))
    
    form = RegisterForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            if User.is_email_taken(form.email.data):
                flash('이메일이 이미 가입되어 있습니다.')
            elif User.is_username_taken(form.username.data):
                flash('아이디가 이미 가입되어 있습니다.')
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
                
                # commented until email verification is set up: return redirect(url_for('user.verify'))
                login_user(new_user)
                return redirect(url_for('home.home'))
                
            return render_template('/register.html', form=form, page=page)
        else:
            return render_template('/register.html', form=form, page=page)
    elif request.method == 'GET':
        return render_template('/register.html', form=form, page=page)

@user_blueprint.route('/verify')
def verify():
    return render_template('/verify.html')

@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    page='login'
    if current_user.is_authenticated:
        flash('이미 로그인된 상태입니다.')
        return redirect(url_for('home.home'))
    
    form = LoginForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            user, authenticated = User.authenticate(form.username.data, form.password.data)
            if user:
                if authenticated:
                    login_user(user, remember=form.remember_me.data)
                    return redirect(url_for('home.home'))
                else:
                    flash('아이디와 비밀번호가 일치하지 않습니다')
                    return render_template('/login.html', form=form, page=page)
            else:
                flash('아이디가 가입되어있지 않습니다')
                return render_template('/login.html', form=form, page=page)
        else:
            return render_template('/login.html', form=form, page=page)
    elif request.method == 'GET':
        return render_template('/login.html', form=form, page=page)

@user_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.home'))

@user_blueprint.route('/profile')
@login_required
def profile():
    return render_template('/profile.html')

