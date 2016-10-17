import unittest

from interswellar import app


class ViewsTest(unittest.TestCase):

    """ Tests the views """

    def setUp(self):
        self.app = app.test_client()

    def test_empty_db(self):
        rv = self.app.get('/')
        self.assertNotEqual(rv.data, '')
