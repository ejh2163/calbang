from app import db, bcrypt
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    date_joined = db.Column(db.Date, nullable=False)
    username = db.Column(db.String(60), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    verified = db.Column(db.Boolean, default=0)
    posts = relationship('Post', backref='author')

    def __init__(self, date_joined, username, email, password, verified):
        self.date_joined = date_joined
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.verified = 0

    def __repr__(self):
        return '<User %r>' % self.username
       
       
class Pages(db.Model):
    __tablename__ = 'pages'
    id = db.Column(db.Integer, primary_key=True)
    page_name = db.Column(db.String(12))

    def __init__(self, page_name):
        self.page_name = page_name

    def __repr__(self):
        return '<Page %r>' % self.page_name
 
 
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.Date, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    page_id = db.Column(db.Integer, db.ForeignKey('pages.id'))
    subject = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text)
    
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    parking = db.Column(db.Integer)
    sqft = db.Column(db.Integer)

    def __init__(self, date_posted, author_id, page_id, subject, body, bedrooms, bathrooms, parking, sqft):
        self.date_posted = date_posted
        self.author_id = author_id
        self.page_id = page_id
        self.subject = subject
        self.body = body
        
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.parking = parking
        self.sqft = sqft
        
    def __repr__(self):
        return '<%>' % self.subject