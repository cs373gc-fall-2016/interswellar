import unittest

from interswellar import app, db, load_config

class APITest(unittest.TestCase):
    """ Tests API routes """

    @classmethod
    def setUpClass(cls):
        load_config(os.environ.get('APP_ENV', 'test'))

    