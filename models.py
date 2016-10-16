from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    verified = db.Column(db.Integer)

    def __init__(self, username, email, password, verified):
        self.username = username
        self.email = email
        self.password = password
        self.verified = 0

    def __repr__(self):
        return '<User %r>' % self.username