from flask_wtf import FlaskForm
from wtforms import (BooleanField, TextField, HiddenField, PasswordField,
    DateTimeField, validators, IntegerField, SubmitField)
from wtforms.fields.html5 import EmailField

'''
self.date_posted = date_posted
        self.username = current_user.username
        self.page = page
        self.viewed = viewed
        
        self.subject = subject
        self.body = body
        self.price = price
        
        self.image_ext = image_ext
'''

class EditForm(FlaskForm):  
    subject = TextField('subject', [
        validators.Required(message='아이디를 입력해주세요'),
        ])
    body = TextField('body')
    bedrooms = IntegerField('bedrooms', [
        validators.Required(message='비밀번호를 입력해주세요'),
        ])
    bathrooms = IntegerField('bathrooms', [
        validators.Required(message='비밀번호를 다시 입력해주세요'),
        ])
    parking = IntegerField('parking', [
        validators.Required(message='비밀번호를 다시 입력해주세요'),
        ])
    sqft = IntegerField('sqft', [
        validators.Required(message='비밀번호를 다시 입력해주세요'),
        ])
    year = IntegerField('year', [
        validators.Required(message='비밀번호를 다시 입력해주세요'),
        ])
    submit = SubmitField('등록하기')