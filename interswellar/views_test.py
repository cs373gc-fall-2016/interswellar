import unittest

from interswellar import app


class ViewsTest(unittest.TestCase):

    """ Tests the views """

    def setUp(self):
        self.app = app.test_client()

    def test_empty_db(self):
        rv = self.app.get('/')
        self.assertEqual(rv.data, b"<h1>My God, it\'s full of stars!</h1>")
