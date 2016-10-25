from flask_wtf import FlaskForm
from wtforms import (BooleanField, TextField, HiddenField, PasswordField,
    DateTimeField, validators, IntegerField, SubmitField)
from wtforms.fields.html5 import EmailField


class EditForm(FlaskForm):  
    username = TextField('username', [
        validators.Required(message='아이디를 입력해주세요'),
        validators.Length(
            min=3, 
            max=30, 
            message='3 ~ 30글자로 입력해주세요'), 
        validators.Regexp(
            "^[a-zA-Z0-9]*$", 
            message="문자나 숫자로만 입력해주세요")
        ])
    email = EmailField('email', [
        validators.Required(message='이메일을 입력해주세요'), 
        validators.Email()
        ])
    password = PasswordField('password', [
        validators.Required(message='비밀번호를 입력해주세요'),
        validators.Length(
            min=6,
            max=120, message='보안을 위해 6자 이상으로 입력해주세요')
        ])
    password_check = PasswordField('password_check', [
        validators.Required(message='비밀번호를 다시 입력해주세요'),
        validators.EqualTo(
            'password', 
            message='비밀번호가 일치하지 않습니다')
        ])
    tc_check = BooleanField('tc-check', [
        validators.Required(message='이용약관에 동의해주세요')
        ])
    submit = SubmitField('가입하기')