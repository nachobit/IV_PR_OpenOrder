import os

# default config
class BaseConfig(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = False
    # shortened for readability
    SECRET_KEY = 'somethingelse-here'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    #SQLALCHEMY_DATABASE_URI = ''
    #app.secret_key='somethingelse'
    print SQLALCHEMY_DATABASE_URI


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    #WTF_CSRF_ENABLED = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False