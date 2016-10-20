#pylint: disable=missing-docstring,unused-variable
import unittest
from interswellar import app
import interswellar.views as views

class ViewsTest(unittest.TestCase):

    """ Tests the views """

    def setUp(self):
        self.app = app.test_client()

    def test_empty_db(self):
        view = self.app.get('/')
        self.assertNotEqual(view.data, '')

    def test_get_commits_size(self):
        commits = views.get_commits()
        self.assertEqual(len(commits), 6)

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
        print(issues)
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
        print(issues)
        self.assertTrue(issues > -1)