""" The flask app """

from flask import Flask

# pylint: disable=C0103
app = Flask(__name__)

# pylint: disable=C0413
# pylint: disable=R0401
import interswellar.views
