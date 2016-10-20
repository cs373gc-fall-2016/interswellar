#pylint: skip-file
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


import interswellar.views
