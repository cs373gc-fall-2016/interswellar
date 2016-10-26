""" Launch the application """
import os
from interswellar import app as application
from interswellar import load_config

load_config(os.environ.get('APP_ENV', 'dev'))

if __name__ == "__main__":
    application.config["JSON_SORT_KEYS"] = False 
    application.run()
