# pylint: skip-file
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import interswellar.config as config

app = Flask(__name__)
app.config.from_object(config.DefaultConfig)
db = SQLAlchemy(app)


def load_config(app_env):
    configs = {
        'dev': config.DevelopmentConfig,
        'ci': config.IntegrationConfig,
        'test': config.TestingConfig,
        'prod': config.ProductionConfig
    }
    app.config.from_object(configs[app_env])
    print("Loading %s configuration: Using db '%s@%s/%s'" % (
        app_env,
        db.engine.url.username,
        db.engine.url.host,
        db.engine.url.database
    ))


import interswellar.views
