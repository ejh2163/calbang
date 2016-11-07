from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_wtf.csrf import CsrfProtect
from flask_mail import Mail
from functools import wraps
from flask import redirect, url_for

db = SQLAlchemy()

login_manager = LoginManager()

csrf = CsrfProtect()

mail = Mail()

# decorator to check if account if verified
def verify_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.verified==0:
            return redirect(url_for('user.unverified'))
        return func(*args, **kwargs)
    return decorated_function
