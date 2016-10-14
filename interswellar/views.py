""" The views for the app """

from interswellar import app


@app.route('/')
def index():
    """ Returns 'My God, it's full of stars!' """
    return "<h1>My God, it\'s full of stars!</h1>"
