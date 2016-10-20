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

@app.route('/stars')
def stars():
	""" Returns stars page """
	data = '[{"id": 1, "author": "Pete Hunt", "text": "This is one comment", "lol":"ghi"}, {"id": 2, "author": "Jordan Walke", "text": "This is *another* comment", "lol":"ghi"}, {"id": 3, "author": "Jordan Walke", "text": "This is *another* comment", "lol":"ghi"}]'
	return render_template('tables.html', data=data, title="STARS")