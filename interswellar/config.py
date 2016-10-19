''' Configurations for different environments '''

# pylint:disable=too-few-public-methods
class Config(object):
    ''' Default configuration '''
    TESTING = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# pylint:disable=too-few-public-methods
class TestingConfig(Config):
    ''' Setting testing flag '''
    TESTING = True

# pylint:disable=too-few-public-methods
class DevelopmentConfig(Config):
    ''' Setting debug flag '''
    DEBUG = True
