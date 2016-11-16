""" The public views for the app """
# pylint:disable=invalid-name,import-error

from collections import defaultdict
import json
import traceback
import html

import requests
from flask import Blueprint, render_template, current_app

import interswellar.models as models

public_views = Blueprint('public_views', __name__)


@public_views.route('/')
def index():
    """ Returns splash page """
    return render_template('index.html')


@public_views.route('/star')
@public_views.route('/stars')
def stars():
    """ Returns stars page """
    return render_template('star_tables.html')


@public_views.route('/star/<int:variable>')
@public_views.route('/stars/<int:variable>')
def star(variable):
    """ Returns page for a single star """
    data = models.Star.query.get(variable)
    if not data:
        return render_template('404.html', thing='Star')
    return render_template('star_detail.html', data=data)


@public_views.route('/exoplanet')
@public_views.route('/exoplanets')
def exoplanets():
    """ Returns exoplanets page """
    return render_template('exoplanet_tables.html')


@public_views.route('/exoplanet/<int:variable>')
@public_views.route('/exoplanets/<int:variable>')
def exoplanet(variable):
    """ Returns page for single exoplanet """
    data = models.Exoplanet.query.get(variable)
    if not data:
        return render_template('404.html', thing='Exoplanet')
    return render_template('exoplanet_detail.html', data=data)


@public_views.route('/constellation')
@public_views.route('/constellations')
def constellations():
    """ Returns constellations page """

    return render_template('constellation_tables.html')


@public_views.route('/constellation/<int:variable>')
@public_views.route('/constellations/<int:variable>')
def constellation(variable):
    """ Returns page for single constellation """

    data = models.Constellation.query.get(variable)
    if not data:
        return render_template('404.html', thing='Constellation')
    return render_template('constellation_detail.html', data=data)


@public_views.route('/publication')
@public_views.route('/publications')
def publications():
    """ Returns publications page """

    return render_template('publication_tables.html')


@public_views.route('/card')
def card():
    """ Returns publications page """

    return render_template('card.html')


@public_views.route('/publication/<int:variable>')
@public_views.route('/publications/<int:variable>')
def publication(variable):
    """ Returns page for single publication """

    data = models.Publication.query.get(variable)
    if not data:
        return render_template('404.html', thing='Publication')
    return render_template('publication_detail.html', data=data)


@public_views.route('/about')
def about():
    """ Returns about page with commit and issues count"""

    commits = get_commits()
    issues = get_issues()
    return render_template('about.html',
                           charlotte_commits=commits[
                               0].get('charharharhar', 0),
                           sami_commits=commits[0].get('TheFireFerret', 0),
                           denise_commits=commits[0].get('denisely', 0),
                           young_commits=commits[0].get('jedyobidan', 0),
                           david_commits=commits[0].get('dshimo', 0),
                           nathan_commits=commits[0].get('nazopo', 0),
                           charlotte_issues=issues[0].get('charharharhar', 0),
                           sami_issues=issues[0].get('TheFireFerret', 0),
                           denise_issues=issues[0].get('denisely', 0),
                           young_issues=issues[0].get('jedyobidan', 0),
                           david_issues=issues[0].get('dshimo', 0),
                           nathan_issues=issues[0].get('nazopo', 0),
                           total_commits=commits[1],
                           total_issues=issues[1])


@public_views.route('/checkdb')
def checkdb():
    """ Queries the db for some stars to see if it's okay"""
    try:
        all_stars = models.Star.query.limit(5).all()

        return 'Database returned the following stars:<br>%s' %  \
            '<br>'.join(html.escape(s.__repr__()) for s in all_stars)
    except Exception:  # pylint:disable=broad-except
        traceback.print_exc()
        return 'Database is not ok. Check stdout for details'


@public_views.route('/tests/run')
def run_tests():
    """ Runs all the unittests and returns the text result with verbosity 2 """
    import interswellar.test_runner as test_runner
    return test_runner.run_tests()


@public_views.route('/search')
def search_results():
    """ takes user search input and renders the and and or search results """
    terms = request.args.get('q')

    return render_template('search.html', terms=terms)


@public_views.errorhandler(404)
def page_not_found(_):
    """ 404 page"""
    return render_template('404.html', thing='Page'), 404


def get_commits():
    """ gets number of commits for each team member """
    user_result = {}

    url = 'https://api.github.com/repos/cs373gc-fall-2016/interswellar/' \
          'stats/contributors?client_id=%s&client_secret=%s' % (
              current_app.config['GITHUB_CLIENT_ID'],
              current_app.config['GITHUB_CLIENT_SECRET'],
          )
    response = requests.get(url).text
    parsed = json.loads(response)
    total = 0

    for user in parsed:
        user_result[user['author']['login']] = user['total']
        total += user['total']

    return [user_result, total]


def get_issues():
    """ get number of issues for each team member """
    num_issues = defaultdict(int)
    total = 0

    for num in range(1, 4):
        url = 'https://api.github.com/repos/cs373gc-fall-2016/interswellar/' \
              'issues?filter=all&state=all&client_id=%s&client_secret=%s&page=%s' % (
                  current_app.config['GITHUB_CLIENT_ID'],
                  current_app.config['GITHUB_CLIENT_SECRET'],
                  num
              )

        response = requests.get(url).text
        parsed = json.loads(response)
        for issue in parsed:
            if 'pull_request' not in issue:
                total += 1
                num_issues[issue['user']['login']] += 1
    return [num_issues, total]
