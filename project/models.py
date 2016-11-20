from flask_login import UserMixin
from project import db
from werkzeug import generate_password_hash, check_password_hash
from flask_login import current_user

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    date_joined = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    verified = db.Column(db.Boolean, nullable=False)
    
    def __init__(self, date_joined, email, username, password, verified):
        self.date_joined = date_joined
        self.email = email
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:sha256:100000')
        self.verified = 0
    
    def __repr__(self):
        return '<User %r>' % self.username

    def set_password(self, password_input):
        self.password = generate_password_hash(password_input)

    def check_password(self, password_input):
        if self.password is None:
            return False
        return check_password_hash(self.password, password_input)

    @classmethod
    def authenticate(cls, username, password):
        user = User.query.filter(db.or_(User.username == username)).first()
        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False
        return user, authenticated
      
    @classmethod
    def is_username_taken(cls, username):
        return db.session.query(db.exists().where(User.username==username)).scalar()
    
    @classmethod
    def is_email_taken(cls, email):
        return db.session.query(db.exists().where(User.email==email)).scalar()


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False)
    username = db.Column(db.String(120), nullable=False)
    page = db.Column(db.String(12), nullable=False)
    viewed = db.Column(db.Integer, nullable=False, default=0)
    subject = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable=False)
    phone = db.Column(db.String(12))
    email = db.Column(db.String(120))
    kakaotalk = db.Column(db.String(30))
    city = db.Column(db.String(24), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image_ext = db.Column(db.String(240), default='/static/images/no-photo.png')
    
    address = db.Column(db.String(240))
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    parking = db.Column(db.Integer)
    utilities = db.Column(db.String(6))
    internet = db.Column(db.String(6))
    furniture = db.Column(db.String(6))
    food = db.Column(db.String(6))
    sqft = db.Column(db.Integer)
    year = db.Column(db.Integer)
    
    def __init__(self, date_posted, username, page, viewed, subject, body, 
                phone, email, kakaotalk, city, price, image_ext, address, 
                bedrooms, bathrooms, parking, utilities, internet, furniture, food, 
                sqft, year):
        self.date_posted = date_posted
        self.username = username
        self.page = page
        self.viewed = viewed
        self.subject = subject
        self.body = body
        self.phone = phone
        self.email = email
        self.kakaotalk = kakaotalk
        self.city = city
        self.price = price
        self.image_ext = image_ext
        
        self.address = address
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.parking = parking
        self.utilities = utilities
        self.internet = internet
        self.furniture = furniture
        self.food = food
        self.sqft = sqft
        self.year = year
        
    def __repr__(self):
        return '<%>' % self.subject
