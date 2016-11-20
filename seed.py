from project.models import User, Post
from project import app, db
import datetime
from time import strftime
import os

# Add seed data to the database
with app.app_context():
    newuser = User(
                date_joined = strftime("%Y-%m-%d"),
                email = 'ejh2163@gmail.com',
                username = 'ejh2163',
                password = '48cd3f6p',
                verified = 1
                )
    newpost_bnb1 = Post(
                date_posted=datetime.datetime.now(), 
                username='admin', 
                page='bnb', 
                viewed=0, 
                subject='민박 샘플 포스팅입니다2', 
                body='민박 샘플 포스팅입니다', 
                phone='123-456-7890', 
                email='calbang.noreply@gmail.com', 
                kakaotalk='calbang', 
                city='Fullerton, CA', 
                price='50', 
                image_ext=None,
                address='1234 Wilshire Blvd.', 
                bedrooms=0, 
                bathrooms=0, 
                parking=1, 
                utilities=None, 
                internet=None,
                furniture=None, 
                food=None, 
                sqft=1234, 
                year=1991
                )
    newpost_bnb2 = Post(
                date_posted=datetime.datetime.now(), 
                username='admin', 
                page='bnb', 
                viewed=0, 
                subject='민박 샘플 포스팅입니다2', 
                body='민박 샘플 포스팅입니다', 
                phone='123-456-7890', 
                email='calbang.noreply@gmail.com', 
                kakaotalk='calbang', 
                city='Los Angeles, CA', 
                price='100', 
                image_ext=None,
                address='1234 Wilshire Blvd.', 
                bedrooms=0, 
                bathrooms=0, 
                parking=1, 
                utilities=None, 
                internet=None,
                furniture=None, 
                food=None, 
                sqft=1234, 
                year=1991
                )
    newpost_homestay = Post(
                date_posted=datetime.datetime.now(), 
                username='admin', 
                page='homestay', 
                viewed=0, 
                subject='하숙 샘플 포스팅입니다2', 
                body='하숙 샘플 포스팅입니다', 
                phone='123-456-7890', 
                email='calbang.noreply@gmail.com', 
                kakaotalk='calbang', 
                city='Los Angeles, CA', 
                price='725', 
                image_ext='',
                address='1234 Wilshire Blvd.', 
                bedrooms=1, 
                bathrooms=0, 
                parking=1, 
                utilities=None, 
                internet=None,
                furniture=None, 
                food=None, 
                sqft=1234, 
                year=1991
                )
                
    db.session.add(newpost_bnb1)
    db.session.add(newpost_bnb2)
    db.session.add(newuser)
    db.session.commit()