import unittest
import os

from interswellar import app, db, load_config

import interswellar.models as models


class ModelsTest(unittest.TestCase):

    """ Tests the models """

    @classmethod
    def setUpClass(cls):
        load_config(os.environ.get('APP_ENV', 'test'))

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.close()
        db.drop_all()

    def test_stars(self):
        star = models.Star(id=1, name='Sun', mass=1.0,
                           luminosity=1.0, temperature=5000, radius=1.0)
        db.session.add(star)
        db.session.commit()
        stars = models.Star.query.all()
        self.assertTrue(star in stars)
        self.assertEqual(len(stars), 1)

    def test_exoplant(self):
        exoplanet = models.Exoplanet(
            id=1, name='earth', mass=0.2, radius=1.0, orbital_period=5000, year_discovered=0)
        db.session.add(exoplanet)
        db.session.commit()
        exoplanets = models.Exoplanet.query.all()
        self.assertTrue(exoplanet in exoplanets)
        self.assertEqual(len(exoplanets), 1)

    def test_constellation(self):
        constellation = models.Constellation(
            id=1, name='big dipper', abbrev='big dp', family='arris', meaning='laddle', area=56.54)
        db.session.add(constellation)
        db.session.commit()
        constellations = models.Constellation.query.all()
        self.assertTrue(constellation in constellations)
        self.assertEqual(len(constellations), 1)

    def test_publication(self):
        publication = models.Publication(
            id=1, name='discovery of new star', year=1986, authors='Carl Sagan, Neil Degrasse Tyson', journal='Harvard Stars', abstract='We found a new star.')
        db.session.add(publication)
        db.session.commit()
        publications = models.Publication.query.all()
        self.assertTrue(publication in publications)
        self.assertEqual(len(publications), 1)
