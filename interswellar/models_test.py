import os

from flask_testing import TestCase

from interswellar import create_app
from interswellar.models import db, Star, Exoplanet, Constellation, Publication


class ModelsTest(TestCase):

    """ Tests the models """

    def create_app(self):
        return create_app(os.environ.get('APP_ENV', 'dev') + '_test')

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_stars1(self):
        star1 = Star(id=1, name='Sun', mass=1.0,
                     luminosity=1.0, temperature=5000, radius=1.0)
        star2 = Star(id=3, name='Lummes', mass=5.0,
                     luminosity=3.0, temperature=6000, radius=2.7)
        db.session.add(star1)
        db.session.add(star2)
        db.session.commit()
        stars = Star.query.all()
        self.assertTrue(star1 in stars)
        self.assertTrue(star2 in stars)
        self.assertEqual(len(stars), 2)

    def test_stars2(self):
        star = Star(id=2, name='Aries', mass=3.0,
                    luminosity=4.0, temperature=7000, radius=3.0)
        db.session.add(star)
        db.session.commit()
        stars = Star.query.all()
        self.assertTrue(star in stars)
        self.assertEqual(stars[0].id, 2)
        self.assertEqual(stars[0].radius, 3.0)

    def test_stars3(self):
        star = Star(id=2, name='Aries', mass=3.0,
                    luminosity=4.0, temperature=7000, radius=3.0)
        db.session.add(star)
        db.session.commit()
        stars = Star.query.all()
        self.assertTrue(star in stars)
        self.assertEqual(stars[0].name, 'Aries')

    def test_stars4(self):
        star1 = Star(id=2, name='Aries', mass=3.0,
                     luminosity=4.0, temperature=7000, radius=3.0)
        star2 = Star(id=3, name='Lummes', mass=5.0,
                     luminosity=3.0, temperature=6000, radius=2.7)
        constellation = Constellation(
            id=1, name='big dipper', abbrev='big dp',
            family='arris', meaning='laddle', area=56.54)
        constellation.stars = [star1, star2]
        db.session.add(star1)
        db.session.add(star2)
        db.session.add(constellation)
        db.session.commit()
        constellations = Constellation.query.all()
        self.assertIn(star1, constellations[0].stars)
        self.assertIn(star2, constellations[0].stars)

    def test_exoplant1(self):
        exoplanet1 = Exoplanet(
            id=1, name='Earth', mass=0.2, radius=1.0, orbital_period=5000, year_discovered=0)
        exoplanet2 = Exoplanet(
            id=2, name='Jupiter', mass=0.4, radius=2.0, orbital_period=8000, year_discovered=12)
        db.session.add(exoplanet1)
        db.session.add(exoplanet2)
        db.session.commit()
        exoplanets = Exoplanet.query.all()
        self.assertTrue(exoplanet1 in exoplanets)
        self.assertTrue(exoplanet2 in exoplanets)
        self.assertEqual(len(exoplanets), 2)

    def test_exoplanet2(self):
        exoplanet = Exoplanet(
            id=1, name='Earth', mass=0.2, radius=1.0, orbital_period=5000, year_discovered=0)
        db.session.add(exoplanet)
        db.session.commit()
        db_exoplanet = Exoplanet.query.first()
        self.assertEqual(db_exoplanet.radius, 1.0)
        self.assertEqual(db_exoplanet.year_discovered, 0)

    def test_exoplanet3(self):
        exoplanet = Exoplanet(
            id=1, name='Earth', mass=0.2, radius=1.0, orbital_period=5000, year_discovered=0)
        db.session.add(exoplanet)
        db.session.commit()
        db_exoplanet = Exoplanet.query.first()
        self.assertEqual(db_exoplanet.name, 'Earth')

    def test_exoplanet4(self):
        exoplanet1 = Exoplanet(
            id=1, name='Earth', mass=0.2, radius=1.0, orbital_period=5000, year_discovered=0)
        exoplanet2 = Exoplanet(
            id=2, name='Jupiter', mass=0.4, radius=2.0, orbital_period=8000, year_discovered=12)
        star = Star(id=2, name='Aries', mass=3.0,
                    luminosity=4.0, temperature=7000, radius=3.0)
        star.exoplanets = [exoplanet1, exoplanet2]
        db.session.add(exoplanet1)
        db.session.add(exoplanet2)
        db.session.add(star)
        db.session.commit()
        db_star = Star.query.first()
        self.assertIn(exoplanet1, db_star.exoplanets)
        self.assertIn(exoplanet2, db_star.exoplanets)

    def test_constellation1(self):
        constellation1 = Constellation(
            id=1, name='big dipper', abbrev='big dp', family='arris', meaning='laddle', area=56.54)
        constellation2 = Constellation(
            id=2, name='little dipper', abbrev='small dp', family='arris', meaning='laddle', area=54.56)
        db.session.add(constellation1)
        db.session.add(constellation2)
        db.session.commit()
        constellations = Constellation.query.all()
        self.assertTrue(constellation1 in constellations)
        self.assertTrue(constellation2 in constellations)
        self.assertEqual(len(constellations), 2)

    def test_constellation2(self):
        constellation = Constellation(
            id=1, name='big dipper', abbrev='big dp', family='arris', meaning='laddle', area=56.54)
        db.session.add(constellation)
        db.session.commit()
        db_constellation = Constellation.query.first()
        self.assertEqual(db_constellation.id, 1)
        self.assertEqual(db_constellation.area, 56.54)

    def test_constellation3(self):
        constellation = Constellation(
            id=1, name='big dipper', abbrev='big dp', family='arris', meaning='laddle', area=56.54)
        db.session.add(constellation)
        db.session.commit()
        db_constellation = Constellation.query.first()
        self.assertEqual(db_constellation.name, 'big dipper')

    def test_constellation4(self):
        constellation1 = Constellation(
            id=1, name='big dipper', abbrev='big dp', family='arris', meaning='laddle', area=56.54)
        constellation2 = Constellation(
            id=2, name='little dipper', abbrev='small dp', family='arris', meaning='laddle', area=54.56)
        publication = Publication(
            id=1, title='discovery of new star', year=1986, authors='Carl Sagan, Neil Degrasse Tyson', journal='Harvard Stars', abstract='We found a new star.')
        publication.constellations = [constellation1, constellation2]
        db.session.add(constellation1)
        db.session.add(constellation2)
        db.session.add(publication)
        db_publication = Publication.query.first()
        self.assertIn(constellation1, db_publication.constellations)
        self.assertIn(constellation2, db_publication.constellations)

    def test_publication1(self):
        publication1 = Publication(
            id=1, title='discovery of new star', year=1986, authors='Carl Sagan, Neil Degrasse Tyson', journal='Harvard Stars', abstract='We found a new star.')
        publication2 = Publication(
            id=2, title='discovery of a new fart', year=1995, authors='Rick and Morty', journal='Harvard Astronomy', abstract='We found a new fart.')
        db.session.add(publication1)
        db.session.add(publication2)
        db.session.commit()
        publications = Publication.query.all()
        self.assertTrue(publication1 in publications)
        self.assertTrue(publication2 in publications)
        self.assertEqual(len(publications), 2)

    def test_publication2(self):
        publication = Publication(
            id=1, title='discovery of new star', year=1986, authors='Carl Sagan, Neil Degrasse Tyson', journal='Harvard Stars', abstract='We found a new star.')
        db.session.add(publication)
        db.session.commit()
        db_publication = Publication.query.first()
        self.assertEqual(db_publication.id, 1)
        self.assertEqual(db_publication.year, 1986)

    def test_publication3(self):
        publication = Publication(
            id=1, title='discovery of new star', year=1986, authors='Carl Sagan, Neil Degrasse Tyson', journal='Harvard Stars', abstract='We found a new star.')
        db.session.add(publication)
        db.session.commit()
        db_publication = Publication.query.first()
        self.assertEqual(db_publication.title, 'discovery of new star')

    def test_publication4(self):
        exoplanet1 = Exoplanet(
            id=1, name='Earth', mass=0.2, radius=1.0, orbital_period=5000, year_discovered=0)
        exoplanet2 = Exoplanet(
            id=2, name='Jupiter', mass=0.4, radius=2.0, orbital_period=8000, year_discovered=12)
        publication = Publication(
            id=1, title='discovery of new star', year=1986, authors='Carl Sagan, Neil Degrasse Tyson', journal='Harvard Stars', abstract='We found a new star.')
        publication.exoplanets = [exoplanet1, exoplanet2]
        db.session.add(exoplanet1)
        db.session.add(exoplanet2)
        db.session.commit()
        db_publication = Publication.query.first()
        self.assertIn(exoplanet1, db_publication.exoplanets)
        self.assertIn(exoplanet2, db_publication.exoplanets)