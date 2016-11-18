import os

from flask_testing import TestCase

from interswellar import create_app
import interswellar.views as views
from interswellar.models import db, Star, Exoplanet, Constellation, Publication



class ViewsTest(TestCase):

    """ Tests the views """

    def create_app(self):
        return create_app(os.environ.get('APP_ENV', 'dev') + '_test')

    def setUp(self):
        db.create_all()
        self.populateDB()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def populateDB(self):
        star1 = Star(
            id=1, name='rouge_star', mass=1.0, luminosity=1.0, temperature=1000,
            radius=1.0
        )
        star2 = Star(
            id=2, name='star',  mass=2.0, luminosity=2.0, temperature=2000,
            radius=2.0
        )
        planet1 = Exoplanet(
            id=1, name='earth',  mass=1.0, radius=1.0, orbital_period=365,
            year_discovered=0
        )
        planet2 = Exoplanet(
            id=2, name='planet', mass=1.0, radius=1.0, orbital_period=1000000,
            year_discovered=2000
        )
        planet3 = Exoplanet(
            id=3, name='jonathan', mass=88.8, radius=44.4, orbital_period=0,
            year_discovered=1994
        )
        constel1 = Constellation(
            id=1, name='little_dipper', abbrev='ld', family='dd',
            meaning='Little Dipper', area=100
        )
        constel2 = Constellation(
            id=2, name='big_dipper',    abbrev='bd', family='dd',
            meaning='Big Dipper',    area=300
        )
        publ1 = Publication(
            id=1, ref='2008A&A...474..293B', title='Local Star Discovered',
            authors='Neil deGrasse Tyson', journal='Astronomy & Astrophysics',
            abstract='Former toaster in sky is actually a star'
        )
        publ2 = Publication(
            id=2, ref='2009A&A...434..421A', title='Bountiful Discoveries made',
            authors='Monkey Monkey, Bill Nye', journal='Astronomy & Astrophysics',
            abstract='This publication lists discoveries of constellation, planets, and stars'
        )

        planet3.star = star1
        planet3.discovered_by = publ2
        publ1.exoplanets = [planet1, planet2]
        publ1.stars = [star1, star2]
        star2.exoplanets = [planet1, planet2]
        constel1.stars = [star1, star2]

        db.session.add(star1)
        db.session.add(star2)
        db.session.add(planet1)
        db.session.add(planet2)
        db.session.add(planet3)
        db.session.add(constel1)
        db.session.add(constel2)
        db.session.add(publ1)
        db.session.add(publ2)
        db.session.commit()


    def test_index(self):
        view = self.client.get('/')
        self.assertEqual(view.status, '200 OK')
        self.assertIn('INTERSWELLAR', view.data.decode('utf-8'))

    def test_star_table1(self):
        view = self.client.get('/star')
        self.assertEqual(view.status, '200 OK')
        self.assertIn('STARS', view.data.decode('utf-8'))

    def test_star_table2(self):
        view = self.client.get('/stars')
        self.assertEqual(view.status, '200 OK')
        self.assertIn('STARS', view.data.decode('utf-8'))

    def test_star_detail1(self):
        view = self.client.get('/star/1')
        self.assertEqual(view.status, '200 OK')
        self.assertIn('rouge_star', view.data.decode('utf-8'))
        self.assertIn('1.0', view.data.decode('utf-8'))
        self.assertIn('1000', view.data.decode('utf-8'))

    def test_star_detail2(self):
        view = self.client.get('/stars/2')
        self.assertEqual(view.status, '200 OK')
        self.assertIn('star', view.data.decode('utf-8'))
        self.assertIn('2.0', view.data.decode('utf-8'))
        self.assertIn('2000', view.data.decode('utf-8'))

    def test_exoplanet_table1(self):
        view = self.client.get('/exoplanet')
        self.assertEqual(view.status, '200 OK')
        self.assertIn('EXOPLANETS', view.data.decode('utf-8'))

    def test_exoplanet_table2(self):
        view = self.client.get('/exoplanets')
        self.assertEqual(view.status, '200 OK')
        self.assertIn('EXOPLANETS', view.data.decode('utf-8'))

    def test_exoplanet_detail1(self):
        view = self.client.get('/exoplanet/1')
        self.assertEqual(view.status, '200 OK')
        self.assertIn('exoplanet', view.data.decode('utf-8'))
        self.assertIn('1', view.data.decode('utf-8'))
        self.assertIn('365', view.data.decode('utf-8'))

    def test_exoplanet_detail2(self):
        view = self.client.get('/exoplanets/2')
        self.assertEqual(view.status, '200 OK')
        self.assertIn('exoplanet', view.data.decode('utf-8'))
        self.assertIn('1.0', view.data.decode('utf-8'))
        self.assertIn('1000000', view.data.decode('utf-8'))

    def test_publication_table1(self):
        view = self.client.get('/publication')
        self.assertEqual(view.status, '200 OK')
        self.assertIn('PUBLICATIONS', view.data.decode('utf-8'))

    def test_publication_table2(self):
        view = self.client.get('/publications')
        self.assertEqual(view.status, '200 OK')
        self.assertIn('PUBLICATIONS', view.data.decode('utf-8'))

    def test_publication_detail1(self):
        view = self.client.get('/publication/1')
        self.assertEqual(view.status, '200 OK')
        self.assertIn('publication', view.data.decode('utf-8'))
        self.assertIn('Local Star Discovered', view.data.decode('utf-8'))
        self.assertIn('Neil deGrasse Tyson', view.data.decode('utf-8'))

    def test_publication_detail2(self):
        view = self.client.get('/publication/2')
        self.assertEqual(view.status, '200 OK')
        self.assertIn('publication', view.data.decode('utf-8'))
        self.assertIn('Monkey Monkey, Bill Nye', view.data.decode('utf-8'))
        self.assertIn('Astronomy', view.data.decode('utf-8'))

    def test_constellation_table1(self):
        view = self.client.get('/constellation')
        self.assertEqual(view.status, '200 OK')
        self.assertIn('CONSTELLATIONS', view.data.decode('utf-8'))

    def test_constellation_table2(self):
        view = self.client.get('/constellations')
        self.assertEqual(view.status, '200 OK')
        self.assertIn('CONSTELLATIONS', view.data.decode('utf-8'))

    def test_constellation_detail1(self):
        view = self.client.get('/constellation/1')
        self.assertEqual(view.status, '200 OK')
        self.assertIn('constellation', view.data.decode('utf-8'))
        self.assertIn('little_dipper', view.data.decode('utf-8'))
        self.assertIn('ld', view.data.decode('utf-8'))

    def test_constellation_detail2(self):
        view = self.client.get('/constellation/2')
        self.assertEqual(view.status, '200 OK')
        self.assertIn('constellation', view.data.decode('utf-8'))
        self.assertIn('big_dipper', view.data.decode('utf-8'))
        self.assertIn('bd', view.data.decode('utf-8'))

    def test_not_found(self):
        view = self.client.get('/constellation/5')
        self.assertEqual(view.status, '200 OK')
        self.assertIn('not found', view.data.decode('utf-8'))

    def test_get_commits_contents(self):
        commits = views.get_commits()[0]
        for person in commits.items():
            self.assertEqual(len(person), 2)

    def test_get_commits_numbers(self):
        commits = views.get_commits()[0]
        for person, num in commits.items():
            self.assertTrue(num > -1)

    def test_get_issues_size(self):
        issues = views.get_issues()[0]
        self.assertTrue(len(issues) > -1)

    def test_get_issues_contents(self):
        issues = views.get_issues()[0]
        for person in issues.items():
            self.assertEqual(len(person), 2)

    def test_get_issues_numbers(self):
        commits = views.get_issues()[0]
        for person, num in commits.items():
            self.assertTrue(num > -1)

    def test_get_total_commits_size(self):
        commits = views.get_commits()[1]
        self.assertTrue(commits > -1)

    def test_get_total_issues_size(self):
        issues = views.get_issues()[1]
        self.assertTrue(issues > -1)
