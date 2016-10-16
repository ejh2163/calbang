import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://jlee7737:@localhost/c9'
db = SQLAlchemy(app)

wsgi_app = app.wsgi_app

from routes import *



if __name__ == "__main__":
    app.run(
        host = os.getenv('IP', '0.0.0.0'), 
        port = int(os.getenv('PORT', 8080)),
        debug = True
        )