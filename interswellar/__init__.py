""" All modules related to the application """

import os
from flask import Flask

import interswellar.config as config
from interswellar.models import db
from interswellar.api import bind_api
from interswellar.views import public_views


__CFG__ = {
    'dev':       config.DevelopmentConfig,
    'dev_test':  config.TestingConfig,
    'ci':        config.IntegrationConfig,
    'ci_test':   config.IntegrationConfig,
    'prod':      config.ProductionConfig,
    'prod_test': config.TestingConfig,
}


def create_app(env):
    """ Application factory function """
    if env not in __CFG__:
        raise ValueError("Invalid environment: %s" % env)

    app = Flask(__name__)
    app.config.from_object(__CFG__[env])

    db.init_app(app)
    bind_api(app)
    app.register_blueprint(public_views)

    if not app.config['TESTING']:
        print("Creating app (env = '%s')" % env)
        with app.app_context():
            print("Using db '%s://%s@%s/%s'" % (
                db.engine.url.drivername,
                db.engine.url.username,
                db.engine.url.host,
                db.engine.url.database
            ))

    return app
