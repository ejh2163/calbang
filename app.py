import os
from flask import Flask
from extensions import db, login_manager, csrf

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


from views import *

if __name__ == "__main__":
    app.run()
        #host = os.getenv('IP', '0.0.0.0'), 
        #port = int(os.getenv('PORT', 8080)),
        #)