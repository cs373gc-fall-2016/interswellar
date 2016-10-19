""" The views for the app """
# pylint: disable=unused-import
from interswellar import app
from flask import Flask, render_template

@app.route('/')
def index():
    """ Returns splash page """
    return render_template('index.html')

@app.route('/about')
def about():
    """ Returns about page """
    return render_template('about.html')
