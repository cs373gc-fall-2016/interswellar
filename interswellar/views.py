""" The views for the app """
# pylint: disable=unused-import,bad-continuation,line-too-long,import-error
from collections import defaultdict
import json
import traceback
import html
import requests
from interswellar import app
import interswellar.models as models
from flask import Flask, render_template


@app.route('/')
def index():
    """ Returns splash page """
    return render_template('index.html')


@app.route('/stars')
def stars():
    """ Returns stars page """
    data = '[{"id": 1, "author": "Pete Hunt", "text": "This is one comment", "lol":"ghi"}, {"id": 2, "author": "Jordan Walke", "text": "This is *another* comment", "lol":"ghi"}, {"id": 3, "author": "Jordan Walke", "text": "This is *another* comment", "lol":"ghi"}]'
    return render_template('tables.html', data=data, title="STARS")


@app.route('/stars/<variable>')
def star(variable):
    """ Returns page for a single star """
    data = [
        '{"name": "Kepler-9", "mass": 1.07, "luminosity": 13.9, "temperature": 5777.00, "radius": 1.02, "constellation": "Lyra", "planets": [ "Kepler-9a", "Kepler-9b", "Kepler-9d" ], "discovered_by": "http://adsabs.harvard.edu/abs/2013A%26A...556A.126A"}']
    json_obj = json.loads(data[int(variable) - 1])
    return render_template('star.html', data=json_obj)


@app.route('/exoplanets')
def exoplanets():
    """ Returns exoplanets page """
    data = '[{"id": 1, "author": "Pete Hunt", "text": "This is one comment", "lol":"ghi"}, {"id": 2, "author": "Jordan Walke", "text": "This is *another* comment", "lol":"ghi"}, {"id": 3, "author": "Jordan Walke", "text": "This is *another* comment", "lol":"ghi"}]'
    return render_template('tables.html', data=data, title="EXOPLANETS")


@app.route('/constellations')
def constellations():
    """ Returns constellations page """
    data = '[{"id": 1, "author": "Pete Hunt", "text": "This is one comment", "lol":"ghi"}, {"id": 2, "author": "Jordan Walke", "text": "This is *another* comment", "lol":"ghi"}, {"id": 3, "author": "Jordan Walke", "text": "This is *another* comment", "lol":"ghi"}]'
    return render_template('tables.html', data=data, title="CONSTELLATIONS")


@app.route('/publications')
def publications():
    """ Returns publications page """
    data = '[{"id": 1, "author": "Pete Hunt", "text": "This is one comment", "lol":"ghi"}, {"id": 2, "author": "Jordan Walke", "text": "This is *another* comment", "lol":"ghi"}, {"id": 3, "author": "Jordan Walke", "text": "This is *another* comment", "lol":"ghi"}]'
    return render_template('tables.html', data=data, title="PUBLICATIONS")


@app.route('/about')
def about():
    """ Returns about page with commit and issues count"""
    commits = get_commits()
    issues = get_issues()
    return render_template('about.html',
                           charlotte_commits=commits.get('charharharhar', 0),
                           sami_commits=commits.get('TheFireFerret', 0),
                           denise_commits=commits.get('denisely', 0),
                           young_commits=commits.get('jedyobidan', 0),
                           david_commits=commits.get('dshimo', 0),
                           nathan_commits=commits.get('nazopo', 0),
                           charlotte_issues=issues.get('charharharhar', 0),
                           sami_issues=issues.get('TheFireFerret', 0),
                           denise_issues=issues.get('denisely', 0),
                           young_issues=issues.get('jedyobidan', 0),
                           david_issues=issues.get('dshimo', 0),
                           nathan_issues=issues.get('nazopo', 0))


@app.route('/checkdb')
def checkdb():
    """ Queries the db for some stars to see if it's okay"""
    try:
        all_stars = models.Star.query.limit(5).all()

        return 'Database returned the following stars:<br>%s' %  \
            '<br>'.join(html.escape(s.__repr__()) for s in all_stars)
    except Exception:  # pylint:disable=broad-except
        traceback.print_exc()
        return 'Database is not ok. Check stdout for details'


def get_commits():
    """ gets number of commits for each team member """
    url = 'https://api.github.com/repos/cs373gc-fall-2016/interswellar/stats/contributors?client_id=a857dda6c0869d2bc306&client_secret=e6f54c0cca99ebb7d6bfd5542052ed49638362ea'
    response = requests.get(url).text
    parsed = json.loads(response)
    return {user['author']['login']: user['total'] for user in parsed}


def get_issues():
    """ get number of issues for each team member """
    url = 'https://api.github.com/repos/cs373gc-fall-2016/interswellar/issues?state=all&client_id=a857dda6c0869d2bc306&client_secret=e6f54c0cca99ebb7d6bfd5542052ed49638362ea'
    response = requests.get(url).text
    parsed = json.loads(response)
    num_issues = defaultdict(int)
    for issue in parsed:
        if 'pull_request' not in issue:
            num_issues[issue['user']['login']] += 1
    return num_issues
