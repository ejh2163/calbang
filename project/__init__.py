import os
from flask import Flask
from .extensions import db, login_manager, csrf
from .models import User, Post

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

# flask-sqlalchemy
db.init_app(app)
# flask-login
login_manager.setup_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)
# flask-wtf
csrf.init_app(app)

from project.home.views import home_blueprint
from project.user.views import user_blueprint
from project.post.views import post_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(post_blueprint)

