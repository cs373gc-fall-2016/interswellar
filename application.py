from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return '<h1>Hello From Nathan!</h1>'

if __name__ == "__main__":
    application.debug = True
    application.run()
