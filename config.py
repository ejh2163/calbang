

class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = '\x95\xdc?\xba\xfdO\xde\xb6"\xcdm\x1el3T<\xf0\xd5\x86\xf6\xa4\xfa\x1b\xfb'
    SECURITY_PASSWORD_SALT = 'saltysalt'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://jlee7737:@localhost/calbang'
    
class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ''