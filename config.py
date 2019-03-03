import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_BINDS = {
    'books': SQLALCHEMY_DATABASE_URI,
    'holidays': 'postgres://zmpdweaujlkryj:40a99dec442636a62720dd0ea0694c6149ec70f6e7199d2074415afb58d50bd4@ec2-174-129-224-157.compute-1.amazonaws.com:5432/d790ds9navtmb7
}


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True