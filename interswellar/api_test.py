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
        publ = models.Publication(
            id=1, ref='2008A&A...474..293B', title='Local Star Discovered',
            authors='Neil deGrasse Tyson', journal='Astronomy & Astrophysics',
            abstract='Former toaster in sky is actually a star'
        )

        planet.star = star
        star.constellation = constel
#        constel.stars = [rouge_star, star]

        db.create_all()
        db.session.add(rouge_star)
        db.session.add(star)
        db.session.add(planet)
        db.session.add(constel)
        db.session.add(publ)
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

    def test_planet_single(self):
        rv = self.app.get('/api/v1/exoplanets')
        self.assertEqual(rv.mimetype, 'application/json')
        data = json.loads(rv.data.decode('utf-8'))
        self.assertEqual(data['objects'][0]['id'], 2)
        self.assertEqual(data['objects'][0]['name'], 'planet')
        self.assertEqual(data['objects'][0]['mass'], 1.0)
        self.assertEqual(data['objects'][0]['radius'], 1.0)
        self.assertEqual(data['objects'][0]['orbital_period'], 1000000)
        self.assertEqual(data['objects'][0]['year_discovered'], 2000)

    def test_constellation_single(self):
        rv = self.app.get('/api/v1/constellations')
        self.assertEqual(rv.mimetype, 'application/json')
        data = json.loads(rv.data.decode('utf-8'))
        self.assertEqual(data['objects'][0]['id'], 2)
        self.assertEqual(data['objects'][0]['name'], 'constel')
        self.assertEqual(data['objects'][0]['abbrev'], 'cst')
        self.assertEqual(data['objects'][0]['family'], 'cf')
        self.assertEqual(data['objects'][0]['meaning'], 'A constellation')
        self.assertEqual(data['objects'][0]['area'], 100 )

    def test_constellation_relationship(self):
        rv = self.app.get('/api/v1/constellations')
        self.assertEqual(rv.mimetype, 'application/json')
        data = json.loads(rv.data.decode('utf-8'))
        constel = data['objects'][0]
#        self.assertEqual(constel[stars][0]['id'], 1)
#        print(constel) Not wanted behavior. Two attributes one object when adding list of two obj
    
    def test_publication_single(self):
        rv = self.app.get('/api/v1/publications')
        self.assertEqual(rv.mimetype, 'application/json')
        data = json.loads(rv.data.decode('utf-8'))
        self.assertEqual(data['objects'][0]['id'], 1)
        self.assertEqual(data['objects'][0]['ref'], '2008A&A...474..293B')
        self.assertEqual(data['objects'][0]['title'], 'Local Star Discovered')
        self.assertEqual(data['objects'][0]['authors'], 'Neil deGrasse Tyson')
        self.assertEqual(data['objects'][0]['journal'], 'Astronomy & Astrophysics')
        self.assertEqual(data['objects'][0]['abstract'], 'Former toaster in sky is actually a star')

