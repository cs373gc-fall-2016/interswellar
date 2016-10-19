import unittest

from interswellar import db, app
import interswellar.models as models


class ModelsTest(unittest.TestCase):

    """ Tests the models """

    def setUp(self):
        app.config.from_object('interswellar.config.TestingConfig')
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
