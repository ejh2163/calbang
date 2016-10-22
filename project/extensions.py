from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CsrfProtect

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CsrfProtect()
