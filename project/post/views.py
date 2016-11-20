from flask import Flask, flash, request, render_template, redirect, session, url_for, Blueprint
from flask_login import login_required
from flask_sqlalchemy import *
import math
import datetime

from project.models import Post
from project import db, verify_required
from project.post.edit_forms import EditForm


post_blueprint = Blueprint('post', __name__, template_folder='templates')

# ********************************************************************************
# View for Posts Page
# 
# - url passes in page and page_num
# - filters pass in url parameters, grabbed using request.args.get and adjusts
#   posts query
# ********************************************************************************
@post_blueprint.route('/<page>/<int:page_num>', methods=['GET'])
def posts(page, page_num):
    # request.args url parameters
    pmin = 0
    pmax = 0
    if request.args.get('pmin') and request.args.get('pmax'):
        pmin = int(re.search(r'\d+', request.args.get('pmin')).group())
        pmax = int(re.search(r'\d+', request.args.get('pmax')).group())
    beds = 0
    if request.args.get('beds'):
        beds = request.args.get('beds')
    baths = 0
    if request.args.get('baths'):
        baths = request.args.get('baths')
    city = ''
    if request.args.get('city'):
        city = request.args.get('city')

    # query filter components
    price_min = db.session.query(db.func.min(Post.price)).filter(Post.page==page).scalar()
    price_max = db.session.query(db.func.max(Post.price)).filter(Post.page==page).scalar()
    if pmin and pmax:
        pmin_filtered = pmin
        pmax_filtered = pmax
    else: 
        pmin_filtered = price_min
        pmax_filtered = price_max
    cities = db.session.query(Post.city.distinct().label('city')).filter(Post.page==page).order_by(Post.city).limit(100).all()
    
    # query post and post components
    posts = (Post.query
            .filter(Post.page==page)
            .filter(Post.price>=pmin_filtered)
            .filter(Post.price<=pmax_filtered)
            .filter(Post.bedrooms>=beds)
            .filter(Post.bathrooms>=baths)
            .filter(Post.city.contains(city))
            .order_by(Post.id.desc())
            .offset((page_num-1)*(18)).limit(18).all()
            )
    price_deco = ''
    if page in ['rent','homestay']:
        price_deco = '월'
    elif page=='bnb':
        price_deco = '일'
    
    db.session.close()
    return render_template('/posts.html', 
                            page=page, 
                            page_num=page_num, 
                            price_min=price_min, 
                            price_max=price_max, 
                            pmin_filtered=pmin_filtered, 
                            pmax_filtered=pmax_filtered, 
                            price_deco=price_deco, 
                            cities=cities, 
                            posts=posts, 
                            today=datetime.datetime.now()
                            )
    
@post_blueprint.route('/<page>/view/<int:post_id>')
def view(page, post_id):
    # update post.viewed count
    post = Post.query.filter(Post.id==post_id).first()
    post.viewed += 1
    db.session.commit()
    
    price_deco = ''
    if page in ['rent','homestay']:
        price_deco = '월'
    elif page=='bnb':
        price_deco = '일'
    
    return render_template('/view.html', 
                            page=page,
                            post=post,
                            price_deco=price_deco,
                            today=datetime.datetime.now()
                            )

@post_blueprint.route('/<page>/new', methods=['GET', 'POST'])
@login_required
@verify_required
def new(page):
        
    form = EditForm()
    
    return render_template('edit.html', page=page, form=form)

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