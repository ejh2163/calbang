from flask import Flask, flash, request, render_template, redirect, session, url_for, Blueprint
from project.models import Post


post_blueprint = Blueprint('post', __name__, template_folder='templates')


@post_blueprint.route('/<category>')
def posts(category):
    return render_template('/posts.html', category=category)
    
@post_blueprint.route('/view/<int:post_id>')
def view(post_id):
    return render_template('/view.html')

@post_blueprint.route('/<category>/edit', methods=['GET', 'POST'])
def edit(category):
    if request.method == 'GET':
        return render_template('/edit.html', cat=category)
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
        return render_template('/view.html', cat=category, posts=posts)
    else:
        return render_template(error_page.html)
        