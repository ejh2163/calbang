from flask import Flask, flash, request, render_template, redirect, session, url_for, Blueprint
from flask_login import login_required
from flask_sqlalchemy import *
import math
import datetime

from project.models import Post
from project import db, verify_required
from project.post.edit_forms import EditForm


post_blueprint = Blueprint('post', __name__, template_folder='templates')


@post_blueprint.route('/<page>/<int:page_num>', methods=['GET'])
def posts(page, page_num):
    # query filter components
    price_min = db.session.query(db.func.min(Post.price)).filter(Post.page==page).scalar()
    price_max = db.session.query(db.func.max(Post.price)).filter(Post.page==page).scalar()
    if price_max == None:
        price_max = 0
    regions = db.session.query(Post.region.distinct().label('region')).filter(Post.page==page).order_by(Post.region).limit(100).all()
    
    # query post and post components
    posts = Post.query.filter(Post.page==page).order_by(Post.id.desc()).offset((page_num-1)*(18)).limit(18).all()
    price_suffix = ''
    if page in ['rent','homestay']:
        price_suffix = '/월'
    elif page=='bnb':
        price_suffix = '/일'
    
    return render_template('/posts.html', 
                            page=page, 
                            page_num=page_num, 
                            price_min=price_min, 
                            price_max=price_max, 
                            regions=regions, 
                            posts=posts,
                            price_suffix=price_suffix,
                            today=datetime.datetime.now()
                            )
    
@post_blueprint.route('/<page>/view/<int:post_id>')
@login_required
@verify_required
def view(page, post_id):
    # update post.viewed count
    post = Post.query.filter(Post.id==post_id).first()
    post.viewed += 1
    db.session.commit()
    
    price_suffix = ''
    if page in ['rent','homestay']:
        price_suffix = '/월'
    elif page=='bnb':
        price_suffix = '/일'
    
    return render_template('/view.html', 
                            page=page,
                            post=post,
                            price_suffix=price_suffix,
                            )

@post_blueprint.route('/<page>/edit', methods=['GET', 'POST'])
@login_required
@verify_required
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