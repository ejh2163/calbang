from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CsrfProtect

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = '/login'
login_manager.login_message = '로그인을 먼저 해주세요.'
login_manager.login_message_category = 'warning'
@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

csrf = CsrfProtect()
