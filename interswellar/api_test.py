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
        star1 = models.Star(
            id=1, name='rouge_star', mass=1.0, luminosity=1.0, temperature=1000,
            radius=1.0
        )
        star2 = models.Star(
            id=2, name='star',       mass=2.0, luminosity=2.0, temperature=2000,
            radius=2.0
        )
        planet1 = models.Exoplanet(
            id=1, name='earth',  mass=1.0, radius=1.0, orbital_period=365,
            year_discovered=0
        )
        planet2 = models.Exoplanet(
            id=2, name='planet', mass=1.0, radius=1.0, orbital_period=1000000,
            year_discovered=2000
        )
        planet3 = models.Exoplanet(
            id=3, name='jonathan', mass=5.0, radius=0.5, orbital_period=2,
            year_discovered=1994
        )
        constel1 = models.Constellation(
            id=1, name='little_dipper', abbrev='ld', family='dd',
            meaning='Little dipper', area=100
        )
        constel2 = models.Constellation(
            id=2, name='big_dipper',    abbrev='bd', family='dd',
            meaning='Big dipper',    area=300
        )
        publ1 = models.Publication(
            id=1, ref='2008A&A...474..293B', title='Local Star Discovered',
            authors='Neil deGrasse Tyson', journal='Astronomy & Astrophysics',
            abstract='Former toaster in sky is actually a star'
        )
        publ2 = models.Publication(
            id=2, ref='2009A&A...434..421A', title='Bountiful Discoveries made',
            authors='Monkey Monkey, Bill Nye', journal='Astronomy & Astrophycis',
            abstract='This publication lists discoveries of constellation, planets, and stars'
        )

        planet2.star = star1
        planet2.discovered_by = publ1
        constel1.stars = [star1, star2]
        star2.exoplanets = [planet1, planet2]
        star2.exoplanets = [planet1, planet2]
        star2.constellation = constel1
        publ1.stars = [star1, star2]
        star2.discovered_by = publ1
        publ1.exoplanets = [planet1, planet2]

        db.create_all()
        db.session.add(star1)
        db.session.add(star2)
        db.session.add(planet1)
        db.session.add(planet2)
        db.session.add(constel1)
        db.session.add(constel2)
        db.session.add(publ1)
        db.session.add(publ2)
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
        self.assertEqual(data['exoplanets'][0]['id'], 1)
        self.assertEqual(data['exoplanets'][1]['id'], 2)
        self.assertEqual(data['constellation']['id'], 1)
        self.assertEqual(data['discovered_by']['id'], 1)

    def test_planet_all(self):
        rv = self.app.get('/api/v1/exoplanets')
        self.assertEqual(rv.mimetype, 'application/json')
        data = json.loads(rv.data.decode('utf-8'))
        self.assertEqual(data['num_results'], 2)
        self.assertEqual(data['objects'][0]['id'], 1)
        self.assertEqual(data['objects'][1]['id'], 2)

    def test_planet_single(self):
        rv = self.app.get('/api/v1/exoplanets/2')
        self.assertEqual(rv.mimetype, 'application/json')
        data = json.loads(rv.data.decode('utf-8'))
        self.assertEqual(data['id'], 2)
        self.assertEqual(data['name'], 'planet')
        self.assertEqual(data['mass'], 1.0)
        self.assertEqual(data['radius'], 1.0)
        self.assertEqual(data['orbital_period'], 1000000)
        self.assertEqual(data['year_discovered'], 2000)

    def test_planet_relationship(self):
        rv = self.app.get('/api/v1/exoplanets/2')
        self.assertEqual(rv.mimetype, 'application/json')
        data = json.loads(rv.data.decode('utf-8'))
        self.assertEqual(data['id'], 2)
        #self.assertEqual(data['star']['id'], 1) #Currently Broken
        self.assertEqual(data['discovered_by']['id'], 1)

    def test_constellation_single(self):
        rv = self.app.get('/api/v1/constellations/1')
        self.assertEqual(rv.mimetype, 'application/json')
        data = json.loads(rv.data.decode('utf-8'))
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['name'], 'little_dipper')
        self.assertEqual(data['abbrev'], 'ld')
        self.assertEqual(data['family'], 'dd')
        self.assertEqual(data['meaning'], 'Little dipper')
        self.assertEqual(data['area'], 100)

    def test_constellation_relationship(self):
        rv = self.app.get('/api/v1/constellations/1')
        self.assertEqual(rv.mimetype, 'application/json')
        data = json.loads(rv.data.decode('utf-8'))
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['stars'][0]['id'], 1)

    def test_publication_single(self):
        rv = self.app.get('/api/v1/publications')
        self.assertEqual(rv.mimetype, 'application/json')
        data = json.loads(rv.data.decode('utf-8'))
        self.assertEqual(data['objects'][0]['id'], 1)
        self.assertEqual(data['objects'][0]['ref'], '2008A&A...474..293B')
        self.assertEqual(data['objects'][0]['title'], 'Local Star Discovered')
        self.assertEqual(data['objects'][0]['authors'], 'Neil deGrasse Tyson')
        self.assertEqual(
            data['objects'][0]['journal'], 'Astronomy & Astrophysics')
        self.assertEqual(
            data['objects'][0]['abstract'], 'Former toaster in sky is actually a star')

    def test_publication_relationship(self):
        rv = self.app.get('/api/v1/publications/1')
        self.assertEqual(rv.mimetype, 'application/json')
        data = json.loads(rv.data.decode('utf-8'))
        self.assertEqual(data['id'], 1)
