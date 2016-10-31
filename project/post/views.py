from flask import Flask, flash, request, render_template, redirect, session, url_for, Blueprint
from project.models import Post
from flask_sqlalchemy import *
from project import db
import math

from .edit_forms import EditForm


post_blueprint = Blueprint('post', __name__, template_folder='templates')


@post_blueprint.route('/<page>/<int:page_num>', methods=['GET'])
def posts(page, page_num):
    price_min = db.session.query(db.func.min(Post.price)).filter(Post.page==page).scalar()
    price_max = db.session.query(db.func.max(Post.price)).filter(Post.page==page).scalar()
    
    regions = db.session.query(Post.region.distinct().label('region')).filter(Post.page==page).order_by(Post.region).limit(120).all()
    
    posts = Post.query.filter(Post.page==page).order_by(Post.id.desc()).offset((page_num-1)*(24)).limit(24).all()
    return render_template('/posts.html', 
                            page=page, 
                            page_num=page_num, 
                            price_min=price_min, 
                            price_max=price_max, 
                            regions=regions, 
                            posts=posts
                            )
    
@post_blueprint.route('/view/<int:post_id>')
def view(post_id):
    post = Post.query.filter(Post.id==post_id).first()
    post.viewed += 1
    db.session.commit()
    return render_template('/view.html', post=post)

@post_blueprint.route('/<page>/edit', methods=['GET', 'POST'])
def edit(page):
    
    form = EditForm()
    
    return render_template('edit.html', page=page, form=form)
    '''
    if request.method == 'GET':
        return render_template('/edit.html', page=page)
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
        return render_template('/view.html', page=page, posts=posts)
    else:
        return render_template(error_page.html)
        '''