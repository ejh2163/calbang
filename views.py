from flask import Flask, flash, request, render_template, redirect, session, url_for
from flask_login import login_required, login_user, current_user, logout_user, confirm_login, login_fresh
from app import app
from extensions import db
from models import User, Post
from user_forms import LoginForm, RegisterForm
from werkzeug import generate_password_hash
from time import strftime

@app.route('/')
def home():
    return render_template('/content/home.html')

# ==================================================
# USER MANAGEMENT ROUTES & VIEWS
# ==================================================

@app.route('/register', methods=['GET', 'POST'])
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
                
            return render_template('/content/register.html', form=form)
        else:
            return render_template('/content/register.html', form=form)
    elif request.method == 'GET':
        return render_template('/content/register.html', form=form)

@app.route('/verify')
def verify():
    return render_template('/content/verify.html')

@app.route('/login', methods=['GET', 'POST'])
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
                    return render_template('/content/login.html', form=form)
            else:
                flash('아이디가 가입되지 않았습니다')
                return render_template('/content/login.html', form=form)
        else:
            return render_template('/content/login.html', form=form)
    elif request.method == 'GET':
        return render_template('/content/login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    logout_user()
    return redirect(url_for('home'))

@app.route('/profile')
@login_required
def profile():
    return render_template('/content/profile.html')


# ==================================================
# PAGE ROUTES & VIEWS
# ==================================================
@app.route('/<category>')
def posts(category):
    return render_template('/content/posts.html', category=category)
    
@app.route('/view/<int:post_id>')
def view(post_id):
    return render_template('/content/view.html')

@app.route('/<category>/edit', methods=['GET', 'POST'])
def edit(category):
    if request.method == 'GET':
        return render_template('/content/edit.html', cat=category)
    elif request.method == 'POST':
        listings = {
            'subject': request.form['subject'],
            'region': request.form['region'],
            'phone': request.form['phone'],
            'email': request.form['email'],
            'body': reqwuest.form['body'],
            'homes_type': request.form['homes_type'],
            'homes_price': request.form['homes_price'],
            'homes_bedrooms': request.form['homes_bedrooms'],
            'homes_parking': request.form['homes_parking'],
            'homes_year': request.form['homes_year'],
            'homes_sqft': request.form['homes_sqft'],
        }
        # store data in data store
        # code
        # code 
        return render_template('/content/view.html', cat=category, posts=posts)
    else:
        return render_template(error_page.html)
        