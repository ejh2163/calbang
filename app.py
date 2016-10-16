import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from functools import wraps

app = Flask(__name__)
app.secret_key = '48cd3f6p'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://jlee7737:@localhost/calbang'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect (url_for('login'))
    return wrap
    
from models import *
from views import *

if __name__ == "__main__":
    app.run(
        host = os.getenv('IP', '0.0.0.0'), 
        port = int(os.getenv('PORT', 8080)),
        debug = True
        )