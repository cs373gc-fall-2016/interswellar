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

    def test_stars1(self):
        star = models.Star(id=1, name='Sun', mass=1.0,
                           luminosity=1.0, temperature=5000, radius=1.0)
        db.session.add(star)
        db.session.commit()
        stars = models.Star.query.all()
        self.assertTrue(star in stars)
        self.assertEqual(len(stars), 1)

    def test_stars2(self):
        star1 = models.Star(id=2, name='Aries', mass=3.0,
                            luminosity=4.0, temperature=7000, radius=3.0)
        star2 = models.Star(id=3, name='Lummes', mass=5.0,
                            luminosity=3.0, temperature=6000, radius=2.7)
        db.session.add(star1)
        db.session.add(star2)
        db.session.commit()
        stars = models.Star.query.all()
        self.assertTrue(star1 in stars)
        self.assertTrue(star2 in stars)
        self.assertEqual(len(stars), 2)

    def test_stars3(self):
        star1 = models.Star(id=4, name='Aries', mass=3.0,
                            luminosity=4.0, temperature=7000, radius=3.0)
        star2 = models.Star(id=3, name='Scobe', mass=9.0,
                            luminosity=2.0, temperature=6500, radius=2.5)
        star3 = models.Star(id=7, name='Wishful', mass=5.0,
                            luminosity=8.0, temperature=6900, radius=2.3)
        db.session.add(star1)
        db.session.add(star2)
        db.session.add(star3)
        db.session.commit()
        stars = models.Star.query.all()
        self.assertTrue(star1 in stars)
        self.assertTrue(star2 in stars)
        self.assertTrue(star3 in stars)
        self.assertEqual(len(stars), 3)

    def test_stars4(self):
        star1 = models.Star(id=2, name='Sun', mass=1.0,
                            luminosity=1.0, temperature=5000, radius=1.0)
        star2 = models.Star(id=4, name='Aries', mass=3.0,
                            luminosity=4.0, temperature=7050, radius=3.0)
        star3 = models.Star(id=3, name='Scobe', mass=9.0,
                            luminosity=2.0, temperature=6500, radius=2.5)
        star4 = models.Star(id=7, name='Wishful', mass=5.0,
                            luminosity=8.0, temperature=6900, radius=2.3)
        db.session.add(star1)
        db.session.add(star2)
        db.session.add(star3)
        db.session.add(star4)
        db.session.commit()
        stars = models.Star.query.all()
        self.assertTrue(star1 in stars)
        self.assertTrue(star2 in stars)
        self.assertTrue(star3 in stars)
        self.assertTrue(star4 in stars)
        self.assertEqual(len(stars), 4)

    def test_stars5(self):
        star1 = models.Star(id=2, name='Aries', mass=3.0,
                            luminosity=4.0, temperature=7000, radius=3.0)
        star2 = models.Star(id=3, name='Lummes', mass=5.0,
                            luminosity=3.0, temperature=6000, radius=2.7)
        star3 = models.Star(id=4, name='Forceless', mass=5.0,
                            luminosity=2.0, temperature=9500, radius=2.2)
        star4 = models.Star(id=7, name='Wishful', mass=5.0,
                            luminosity=8.0, temperature=6900, radius=2.3)
        star5 = models.Star(id=8, name='Scobe', mass=9.0,
                            luminosity=2.0, temperature=6500, radius=2.5)
        db.session.add(star1)
        db.session.add(star2)
        db.session.add(star3)
        db.session.add(star4)
        db.session.add(star5)
        db.session.commit()
        stars = models.Star.query.all()
        self.assertTrue(star1 in stars)
        self.assertTrue(star2 in stars)
        self.assertTrue(star3 in stars)
        self.assertTrue(star4 in stars)
        self.assertTrue(star5 in stars)
        self.assertEqual(len(stars), 5)

    def test_stars6(self):
        star1 = models.Star(id=4, name='Aries', mass=3.0,
                            luminosity=4.0, temperature=7000, radius=3.0)
        star2 = models.Star(id=3, name='Scobe', mass=9.0,
                            luminosity=2.0, temperature=6500, radius=2.5)
        star3 = models.Star(id=7, name='Wishful', mass=5.0,
                            luminosity=8.0, temperature=6940, radius=2.3)
        star4 = models.Star(id=9, name='Scobe', mass=9.0,
                            luminosity=2.0, temperature=6500, radius=2.5)
        star5 = models.Star(id=2, name='Spiteful', mass=5.0,
                            luminosity=8.0, temperature=6800, radius=2.9)
        star6 = models.Star(id=5, name='Relentless', mass=5.0,
                            luminosity=8.0, temperature=6100, radius=2.1)
        db.session.add(star1)
        db.session.add(star2)
        db.session.add(star3)
        db.session.add(star4)
        db.session.add(star5)
        db.session.add(star6)
        db.session.commit()
        stars = models.Star.query.all()
        self.assertTrue(star1 in stars)
        self.assertTrue(star2 in stars)
        self.assertTrue(star3 in stars)
        self.assertTrue(star4 in stars)
        self.assertTrue(star5 in stars)
        self.assertTrue(star6 in stars)
        self.assertEqual(len(stars), 6)

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
            id=1, title='discovery of new star', year=1986, authors='Carl Sagan, Neil Degrasse Tyson', journal='Harvard Stars', abstract='We found a new star.')
        db.session.add(publication)
        db.session.commit()
        publications = models.Publication.query.all()
        self.assertTrue(publication in publications)
        self.assertEqual(len(publications), 1)

    def test_star_planet_rel(self):
        star = models.Star(id=2, name='star2', mass=2.0, luminosity=2.0,
                           temperature=2000, radius=2.0)
        planet = models.Exoplanet(id=1, name='planet1', mass=1.0, radius=1.0,
                                  orbital_period=1000000, year_discovered=2000)
        planet.star = star
        db.session.add(star)
        db.session.add(planet)
        db.session.commit()
        star_ret = models.Star.query.first()
        self.assertEqual(star, star_ret)
        self.assertTrue(planet in star.exoplanets)
