""" The views for the app """

from interswellar import app


@app.route('/')
def index():
    """ Returns 'Hello World' """
    return '<h1>Hello from Flask!</h1>'
