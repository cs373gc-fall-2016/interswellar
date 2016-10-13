from interswellar import app

@app.route('/')
def index():
	return '<h1>Hello from Flask!</h1>'