''' The different application configs'''
import os
#pylint:disable=too-few-public-methods
class DefaultConfig(object):
    ''' The default configuration '''
    TESTING = False
    DEBUG = False    
    SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s' % (
        os.environ.get('RDS_USERNAME'),
        os.environ.get('RDS_PASSWORD'),
        os.environ.get('RDS_HOSTNAME'),
        os.environ.get('RDS_PORT'),
        os.environ.get('RDS_DB_NAME')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

#pylint:disable=too-few-public-methods
class IntegrationConfig(DefaultConfig):
    ''' Configuration for Travis CI'''
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:@localhost/interswellar'

#pylint:disable=too-few-public-methods
class DevelopmentConfig(DefaultConfig):
    ''' Configuration for local development '''
    DEBUG = True

class TestingConfig(DefaultConfig):
    ''' Configuration for local testing '''
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'

#pylint:disable=too-few-public-methods
class ProductionConfig(DefaultConfig):
    ''' Configuration for production '''
