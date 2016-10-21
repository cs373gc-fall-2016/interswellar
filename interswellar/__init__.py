# pylint: skip-file
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager

import interswellar.config as config

app = Flask(__name__)
app.config.from_object(config.DefaultConfig)
db = SQLAlchemy(app)
apimanager = APIManager(app, flask_sqlalchemy_db=db)


def load_config(app_env):
    configs = {
        'dev': config.DevelopmentConfig,
        'ci': config.IntegrationConfig,
        'test': config.TestingConfig,
        'prod': config.ProductionConfig
    }
    app.config.from_object(configs[app_env])
    print("Loading %s configuration: Using db '%s://%s@%s/%s'" % (
        app_env,
        db.engine.url.drivername,
        db.engine.url.username,
        db.engine.url.host,
        db.engine.url.database
    ))


import interswellar.views
import interswellar.api