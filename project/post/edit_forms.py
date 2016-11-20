from flask_wtf import FlaskForm
from wtforms import (BooleanField, TextField, HiddenField, PasswordField,
    DateTimeField, validators, IntegerField, SubmitField)
from wtforms.fields.html5 import EmailField

class EditForm(FlaskForm):
    subject = TextField('subject', [
        validators.Required(message='아이디를 입력해주세요'),
        ])
    body = TextField('body', [
        validators.Required(message='아이디를 입력해주세요'),
        ])
    phone = TextField('phone')
    email = EmailField('email', [
        validators.Email()
        ])
    kakaotalk = TextField('kakaotalk')
    city = TextField('city', [
        validators.Required(message='아이디를 입력해주세요'),
        ])
    price = IntegerField('price', [
        validators.Required(message='아이디를 입력해주세요'),
        ])
    image_ext = TextField('image_ext')
    bedrooms = IntegerField('bedrooms', [
        validators.Required(message='비밀번호를 입력해주세요'),
        ])
    bathrooms = IntegerField('bathrooms', [
        validators.Required(message='비밀번호를 다시 입력해주세요'),
        ])
    parking = IntegerField('parking')
    utilities = TextField('utilities')
    internet = TextField('internet')
    furniture = TextField('furniture')
    food = TextField('food')
    sqft = IntegerField('sqft')
    year = IntegerField('year')
    submit = SubmitField('등록하기')