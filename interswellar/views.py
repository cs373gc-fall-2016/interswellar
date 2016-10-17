""" The views for the app """
# pylint: disable=unused-import
from interswellar import app
# from flask import render_template
from flask import Flask, render_template

@app.route('/')
def index():
    """ Returns splash page """
    return render_template('index.html')
