""" The flask app """

from flask import Flask

# pylint: disable=C0103
app = Flask(__name__)

import interswellar.views
