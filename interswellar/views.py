""" The views for the app """
from interswellar import app
from flask import Flask, render_template

import traceback
import html
import interswellar.models as models

@app.route('/')
def index():
    """ Returns splash page """
    return render_template('index.html')


@app.route('/about')
def about():
    """ Returns about page """
    return render_template('about.html')

@app.route('/checkdb')
def checkdb():
    """ Queries the db for some stars to see if it's okay"""
    try:
        stars = models.Star.query.limit(5).all();

        return 'Database returned the following stars:<br>%s' %  \
            '<br>'.join(html.escape(s.__repr__()) for s in stars)
    except:
        traceback.print_exc()
        return 'Database is not ok. Check stdout for details'