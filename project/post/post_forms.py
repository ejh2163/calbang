from flask_wtf import FlaskForm
from wtforms import (BooleanField, TextField, HiddenField, PasswordField,
    DateTimeField, validators, IntegerField, SubmitField)
from wtforms.fields.html5 import EmailField


class EditForm(FlaskForm):  
    search = SubmitField('search')