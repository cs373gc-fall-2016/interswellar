import unittest
import os
import json

from interswellar import app, db, load_config
import interswellar.models as models


class APITest(unittest.TestCase):

    ''' Tests API routes '''

    @classmethod
    def setUpClass(cls):
        load_config(os.environ.get('APP_ENV', 'test'))
        star1 = models.Star(id=1, name='star1', mass=1.0, luminosity=1.0,
                            temperature=1000, radius=1.0)
        star2 = models.Star(id=2, name='star2', mass=2.0, luminosity=2.0,
                            temperature=2000, radius=2.0)

        db.create_all()
        db.session.add(star1)
        db.session.add(star2)
        db.session.commit()

    @classmethod
    def tearDownClass(cls):
        db.session.close()
        db.drop_all()

    def setUp(self):
        self.app = app.test_client()

    def test_stars_all(self):
        rv = self.app.get('/api/v1/stars')
        self.assertEqual(rv.mimetype, 'application/json')
        data = json.loads(rv.data.decode('utf-8'))
        self.assertEqual(data['num_results'], 2)
        self.assertEqual(data['objects'][0]['id'], 1)
        self.assertEqual(data['objects'][1]['id'], 2)

    def test_stars_single(self):
        rv = self.app.get('/api/v1/stars/1')
        self.assertEqual(rv.mimetype, 'application/json')
        data = json.loads(rv.data.decode('utf-8'))
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['name'], 'star1')
        self.assertEqual(data['mass'], 1.0)
        self.assertEqual(data['luminosity'], 1.0)
        self.assertEqual(data['temperature'], 1000)
        self.assertEqual(data['radius'], 1.0)
