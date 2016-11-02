import os

from flask_testing import TestCase

from interswellar import create_app
import interswellar.views as views


class ViewsTest(TestCase):

    """ Tests the views """

    def create_app(self):
        return create_app(os.environ.get('APP_ENV', 'dev') + '_test')

    def test_empty_db(self):
        view = self.client.get('/')
        self.assertEqual(view.status, '200 OK')
        self.assertNotEqual(view.data, '')

    def test_get_commits_contents(self):
        commits = views.get_commits()
        for person in commits.items():
            self.assertEqual(len(person), 2)

    def test_get_commits_numbers(self):
        commits = views.get_commits()
        for person, num in commits.items():
            self.assertTrue(num > -1)

    def test_get_issues_size(self):
        issues = views.get_issues()
        self.assertTrue(len(issues) > -1)

    def test_get_issues_contents(self):
        issues = views.get_issues()
        for person in issues.items():
            self.assertEqual(len(person), 2)

    def test_get_issues_numbers(self):
        commits = views.get_issues()
        for person, num in commits.items():
            self.assertTrue(num > -1)

    def test_get_total_commits_size(self):
        commits = views.get_total_commits()
        self.assertTrue(commits > -1)

    def test_get_total_issues_size(self):
        issues = views.get_total_issues()
        self.assertTrue(issues > -1)
