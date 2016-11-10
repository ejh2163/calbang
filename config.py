import os

class Config(object):
    # main config
    DEBUG = False
    CSRF_ENABLED = True
    SECURITY_PASSWORD_SALT = 'saltysalt'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_POOL_RECYCLE = 60
    
    # mail settings
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    # gmail authentication
    MAIL_USERNAME = os.environ['APP_MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['APP_MAIL_PASSWORD']

    # mail accounts
    MAIL_DEFAULT_SENDER = 'noreply@calbang.com'
    
class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SECRET_KEY = os.environ['SECRET_KEY']
    
class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SECRET_KEY = os.environ['SECRET_KEY']