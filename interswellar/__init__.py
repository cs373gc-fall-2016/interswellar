#pylint: skip-file
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from interswellar.config import get_config

config = get_config(os.environ.get('APP_ENV'))
app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

import interswellar.views
