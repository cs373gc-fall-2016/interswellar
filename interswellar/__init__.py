""" The flask app """

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# pylint: disable=C0103
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# pylint: disable=C0103
db = SQLAlchemy(app)

# pylint: disable=C0413
# pylint: disable=R0401
import interswellar.views
