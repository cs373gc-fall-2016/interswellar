""" The views for the app """

from interswellar import app
from flask import Flask, render_template

@app.route('/')
def index():
    """ Returns 'My God, it's full of stars!' """
    # return "<h1>My God, it\'s full of stars!</h1>"
    return render_template('index.html')
