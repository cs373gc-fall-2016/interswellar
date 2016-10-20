''' The different application configs'''
import os

def get_config(app_env):
    ''' Returns the correct config based on the current environment'''
    configs = {
        'dev': DevelopmentConfig,
        'ci': IntegrationConfig,
        'prod': ProductionConfig
    }
    return configs.get(app_env, configs['dev'])

#pylint:disable=too-few-public-methods
class Config(object):
    ''' The default configuration '''
    TESTING = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

#pylint:disable=too-few-public-methods
class IntegrationConfig(Config):
    ''' Configuration for Travis CI'''
    TESTING = True

#pylint:disable=too-few-public-methods
class DevelopmentConfig(Config):
    ''' Configuration for local development '''
    DEBUG = True

#pylint:disable=too-few-public-methods
class ProductionConfig(Config):
    ''' Configuration for production '''
    SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s' % (
        os.environ.get('RDS_USERNAME'),
        os.environ.get('RDS_PASSWORD'),
        os.environ.get('RDS_HOSTNAME'),
        os.environ.get('RDS_PORT'),
        os.environ.get('RDS_DB_NAME')
    )
