import os

# default config
class BaseConfig(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = False
    # shortened for readability
    SECRET_KEY = 'somethingelse-here'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    #SQLALCHEMY_DATABASE_URI = 'postgres://yebgaqukiltzzs:HE3SqSFyt09HOEtwsvedM7zJvv@ec2-54-83-203-50.compute-1.amazonaws.com:5432/d2qcb810h7i919'
    #app.secret_key='somethingelse'
    print SQLALCHEMY_DATABASE_URI


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    #WTF_CSRF_ENABLED = False
    #SQLALCHEMY_DATABASE_URI = 'postgres://yebgaqukiltzzs:HE3SqSFyt09HOEtwsvedM7zJvv@ec2-54-83-203-50.compute-1.amazonaws.com:5432/d2qcb810h7i919'

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False