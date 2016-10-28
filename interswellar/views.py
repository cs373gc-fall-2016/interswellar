""" The views for the app """
# pylint: disable=unused-import,bad-continuation,line-too-long,import-error
from collections import defaultdict, OrderedDict
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
    data = requests.get('http://interswellar.me/api/v1/stars').json()
    for i in range(0, data['num_results']):
        data['objects'][i] = OrderedDict([('id', data['objects'][i]['id']), ('name', data['objects'][i]['name']), ('luminosity', data['objects'][i]['luminosity']), ('mass', data['objects'][i]['mass']), ('radius', data['objects'][i]['radius']), ('temperature', data['objects'][i]['temperature']), ('constellation', data['objects'][i]['constellation']), ('exoplanets', data['objects'][i]['exoplanets']), ('discovered_by', data['objects'][i]['discovered_by'])])
    return render_template('tables.html', data=data, title="STARS", bg_url='http://apod.nasa.gov/apod/image/1610/TulipNebula_SHO_pugh.jpg')


@app.route('/stars/<int:variable>')
def star(variable):
    """ Returns page for a single star """
    data = requests.get('http://interswellar.me/api/v1/stars/' + str(variable)).json()
    return render_template('star_detail.html', data=data)


@app.route('/exoplanets')
def exoplanets():
    """ Returns exoplanets page """
    data = requests.get('http://interswellar.me/api/v1/exoplanets').json()
    for i in range(0, data['num_results']):
        data['objects'][i] = OrderedDict([('id', data['objects'][i]['id']), ('name', data['objects'][i]['name']), ('mass', data['objects'][i]['mass']), ('radius', data['objects'][i]['radius']), ('orbital_period', data['objects'][i]['orbital_period']), ('year_discovered', data['objects'][i]['year_discovered']), ('star', data['objects'][i]['star']), ('discovered_by', data['objects'][i]['discovered_by'])])
    return render_template('tables.html', data=data, title="EXOPLANETS", bg_url='/static/images/exoplanet.jpg')


@app.route('/exoplanets/<int:variable>')
def exoplanet(variable):
    """ Returns page for single exoplanet """
    data = requests.get('http://interswellar.me/api/v1/exoplanets/' + str(variable)).json()
    return render_template('exoplanet_detail.html', data=data)


@app.route('/constellations')
def constellations():
    """ Returns constellations page """
    data = requests.get('http://interswellar.me/api/v1/constellations').json()
    for i in range(0, data['num_results']):
        data['objects'][i] = OrderedDict([('id', data['objects'][i]['id']), ('abbrev', data['objects'][i]['abbrev']), ('name', data['objects'][i]['name']), ('family', data['objects'][i]['family']), ('meaning', data['objects'][i]['meaning']), ('area', data['objects'][i]['area']), ('stars', data['objects'][i]['stars'])])
    return render_template('tables.html', data=data, title="CONSTELLATIONS", bg_url='/static/images/constellation.jpg')


@app.route('/constellations/<int:variable>')
def constellation(variable):
    """ Returns page for single constellation """
    data = requests.get('http://interswellar.me/api/v1/constellations/' + str(variable)).json()
    return render_template('constellation_detail.html', data=data)


@app.route('/publications')
def publications():
    """ Returns publications page """
    data = requests.get('http://interswellar.me/api/v1/publications').json()

    for i in range(0, data['num_results']):
        data['objects'][i] = OrderedDict([('id', data['objects'][i]['id']), ('ref', data['objects'][i]['ref']), ('title', data['objects'][i]['title']), ('authors', data['objects'][i]['authors']), ('journal', data['objects'][i]['journal']), ('abstract', data['objects'][i]['abstract']), ('stars', data['objects'][i]['stars']), ('exoplanets', data['objects'][i]['exoplanets'])])
    return render_template('tables.html', data=data, title="PUBLICATIONS", bg_url='/static/images/publication.jpg')


@app.route('/publications/<int:variable>')
def publication(variable):
    """ Returns page for single publication """
    data = requests.get('http://interswellar.me/api/v1/publications/' + str(variable)).json()
    return render_template('publication_detail.html', data=data)


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
                           nathan_issues=issues.get('nazopo', 0),
                           total_commits=get_total_commits(),
                           total_issues=get_total_issues())


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


def get_total_commits():
    """ gets number of commits for each team member """
    url = 'https://api.github.com/repos/cs373gc-fall-2016/interswellar/stats/contributors?client_id=a857dda6c0869d2bc306&client_secret=e6f54c0cca99ebb7d6bfd5542052ed49638362ea'
    response = requests.get(url).text
    parsed = json.loads(response)
    total = 0
    for user in parsed:
        total += user['total']
    return total


def get_issues():
    """ get number of issues for each team member """
    url = 'https://api.github.com/repos/cs373gc-fall-2016/interswellar/issues?state=all&filter=all&client_id=a857dda6c0869d2bc306&client_secret=e6f54c0cca99ebb7d6bfd5542052ed49638362ea'
    response = requests.get(url).text
    parsed = json.loads(response)
    num_issues = defaultdict(int)
    for issue in parsed:
        if 'pull_request' not in issue:
            num_issues[issue['user']['login']] += 1
    return num_issues


def get_total_issues():
    """ get number of issues for each team member """
    url = 'https://api.github.com/repos/cs373gc-fall-2016/interswellar/issues?filter=all&state=all&client_id=a857dda6c0869d2bc306&client_secret=e6f54c0cca99ebb7d6bfd5542052ed49638362ea'
    response = requests.get(url).text
    parsed = json.loads(response)
    num_issues = 0
    for issue in parsed:
        if 'pull_request' not in issue:
            num_issues += 1
    return num_issues
