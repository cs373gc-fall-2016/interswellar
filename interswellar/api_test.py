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
        rouge_star = models.Star(
            id=1, name='rouge_star', mass=1.0, luminosity=1.0, temperature=1000,
            radius=1.0
        )

        star = models.Star(
            id=2, name='star', mass=2.0, luminosity=2.0, temperature=2000,
            radius=2.0
        )
        planet = models.Exoplanet(
            id=2, name='planet', mass=1.0, radius=1.0, orbital_period=1000000,
            year_discovered=2000
        )
        constel = models.Constellation(
            id=2, name='constel', abbrev='cst', family='cf',
            meaning='A constellation', area=100
        )

        planet.star = star
        star.constellation = constel

        db.create_all()
        db.session.add(rouge_star)
        db.session.add(star)
        db.session.add(planet)
        db.session.add(constel)
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
        self.assertEqual(data['name'], 'rouge_star')
        self.assertEqual(data['mass'], 1.0)
        self.assertEqual(data['luminosity'], 1.0)
        self.assertEqual(data['temperature'], 1000)
        self.assertEqual(data['radius'], 1.0)

    def test_stars_relationship(self):
        rv = self.app.get('/api/v1/stars/2')
        self.assertEqual(rv.mimetype, 'application/json')
        data = json.loads(rv.data.decode('utf-8'))
        self.assertEqual(data['exoplanets'][0]['id'], 2)
        self.assertEqual(data['constellation']['id'], 2)
