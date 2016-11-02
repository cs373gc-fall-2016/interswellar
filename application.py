""" Launch the application """
import os
from interswellar import create_app

# pylint:disable=invalid-name
application = create_app(os.environ.get('APP_ENV', 'dev'))

if __name__ == "__main__":
    application.config["JSON_SORT_KEYS"] = False
    application.run()
