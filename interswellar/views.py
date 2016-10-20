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


# @app.route('/stars')
# def stars():
#     """ Returns stars page """
#     data = '[{"id": 1, "author": "Pete Hunt", "text": "This is one comment", "lol":"ghi"}, {"id": 2, "author": "Jordan Walke", "text": "This is *another* comment", "lol":"ghi"}, {"id": 3, "author": "Jordan Walke", "text": "This is *another* comment", "lol":"ghi"}]'
#     return render_template('tables.html', data=data, title="STARS")

@app.route('/stars')
def stars():
    """ Returns stars page """
    data = {
            "num_results": 2,
            "objects": [
                {
                    "id": 1,
                    "name": "Kepler-9",
                    "luminosity": 13.9,
                    "mass": 1.07,
                    "radius": 1.02,
                    "temperature": 5777.00,
                    "constellation": {"id": 1, "abbrev": "Lyr"},
                    "exoplanets": [
                        {"id": 1, "name": "Kepler-9a"},
                        {"id": 2, "name": "Kepler-9b"},
                        {"id": 3, "name": "Kepler-9d"}
                    ],
                    "discoverer": {"id": 1, "ref": "2013A&A...566A.126A"}
                },
                {
                    "id": 2,
                    "name": "HIP 64690",
                    "luminosity": 0.810,
                    "mass": 0.95,
                    "radius": 0.93,
                    "temperature": 5679.00,
                    "constellation": {"id": 1, "abbrev": "Oct"},
                    "exoplanets": [],
                    "discoverer": {"id": 1, "ref": "2011A&A...534A..58P"}
                }
            ],
            "page": 1,
            "total_pages": 1
        }
    return render_template('tables.html', data=data, title="STARS")

@app.route('/stars/<variable>')
def star(variable):
    """ Returns page for a single star """
    data = {"id": 1, "name": "Kepler-9", "luminosity": 13.9, "mass": 1.07, "radius": 1.02, "temperature": 5777.00, "constellation": {"id": 1, "abbrev": "Lyr"}, "exoplanets": [{"id": 1, "name": "Kepler-9a"}, {"id": 2, "name": "Kepler-9b"}, {"id": 3, "name": "Kepler-9d"}], "discovered_by": {"id": 1, "ref": "2013A&A...566A.126A"}}
    return render_template('detail.html', data=data)

@app.route('/exoplanets')
def exoplanets():
    """ Returns exoplanets page """
    data = {
            "num_results": 3,
            "objects": [
                {
                    "id": 1,
                    "name": "Kepler-9b",
                    "mass": 80.09,
                    "radius": 9.438,
                    "orbital_period": 1662336,
                    "year_discovered": 2010,
                    "star": {
                        "id": 1,
                        "name": "Kepler-9",
                        "constellation": {"id": 1, "abbrev":"Lyr"}
                    },
                    "discovered_by": {"id": 1, "ref": "2013A&A...566A.126A"}
                },
                {
                    "id": 2,
                    "name": "Kepler-9c",
                    "mass": 54.249,
                    "radius": 9.225,
                    "orbital_period": 3361824,
                    "year_discovered": 2010,
                    "star": {
                        "id": 1,
                        "name": "Kepler-9",
                        "constellation": {"id": 1, "abbrev":"Lyr"}
                    },
                    "discovered_by": {"id": 1, "ref": "2013A&A...566A.126A"}
                },
                {
                    "id": 3,
                    "name": "Kepler-9d",
                    "mass": "unknown",
                    "radius": 1.6,
                    "orbital_period": 137376,
                    "year_discovered": 2010,
                    "star": {
                        "id": 1,
                        "name": "Kepler-9",
                        "constellation": {"id": 1, "abbrev":"Lyr"}
                    },
                    "discovered_by": {"id": 1, "ref": "2013A&A...566A.126A"}
                }
            ],
            "page": 1,
            "total_pages": 1
        }
    return render_template('tables.html', data=data, title="EXOPLANETS")

@app.route('/exoplanets/<variable>')
def exoplanet(variable):
    """ Returns page for single exoplanet """
    data = {
            "id": 2,
            "name": "Kepler-9c",
            "mass": 54.249,
            "radius": 9.225,
            "orbital_period": 3361824,
            "year_discovered": 2010,
            "star": {
                "id": 1,
                "name": "Kepler-9",
                "constellation": {"id": 1, "abbrev":"Lyr"}
            },
            "discovered_by": {"id": 1, "ref": "2013A&A...566A.126A"}
        }
    return render_template('detail.html', data=data)

@app.route('/constellations')
def constellations():
    """ Returns constellations page """
    data = {
            "num_results": 2,
            "objects": [
                {
                    "id": 1,
                    "abbrev": "Lyr",
                    "name": "Lyra",
                    "family": "Hercules",
                    "meaning": "lyre / harp",
                    "area": 286,
                    "stars": [
                        {
                            "id": 1,
                            "name": "Kepler-9",
                            "exoplanets": [
                                {"id": 1, "name": "Kepler-9a"},
                                {"id": 2, "name": "Kepler-9b"},
                                {"id": 3, "name": "Kepler-9d"}
                            ]
                        }
                    ]
                },
                {
                    "id": 2,
                    "abbrev": "Oct",
                    "name": "Octans",
                    "family": "La Caille",
                    "meaning": "octant (instrument)",
                    "area": 291,
                    "stars": [
                        {
                            "id": 2,
                            "name": "HIP 64690",
                            "exoplanets": []
                        }
                    ]
                }
            ],
            "page": 1,
            "total_pages": 1
        }
    return render_template('tables.html', data=data, title="CONSTELLATIONS")

@app.route('/constellations/<variable>')
def constellation(variable):
    """ Returns page for single constellation """
    data = {"id": 1,
            "abbrev": "Lyr",
            "name": "Lyra",
            "family": "Hercules",
            "meaning": "lyre / harp",
            "area": 286,
            "stars": [
                {
                    "id": 1,
                    "name": "Kepler-9",
                    "exoplanets": [
                        {"id": 1, "name": "Kepler-9a"},
                        {"id": 2, "name": "Kepler-9b"},
                        {"id": 3, "name": "Kepler-9d"}
                    ]
                }
            ]
        }
    return render_template('detail.html', data=data)

@app.route('/publications')
def publications():
    """ Returns publications page """
    data = {
            "num_results": 2,
            "objects": [
                {
                    "id": 1,
                    "ref": "2013A&A...566A.126A",
                    "title": "A dynamically-packed planetary system around GJ 667C with three super-Earths in its habitable zone",
                    "authors": "Anglada-Escudé, Guillem; Tuomi, Mikko; Gerlach, Enrico; Barnes, Rory",
                    "journal": "Astronomy & Astrophysics",
                    "abstract": "Context. Since low-mass stars have low luminosities, orbits...",
                    "stars": [
                        {"id": 1, "name": "Kepler-9"}
                    ],
                    "planets": [
                        {"id": 1, "name": "Kepler-9b"},
                        {"id": 2, "name": "Kepler-9c"},
                        {"id": 3, "name": "Kepler-9d"}
                    ]
                },
                {
                    "id": 2,
                    "ref": "2011A&A...534A..58P",
                    "title": "The HARPS search for Earth-like planets in the habitable zone. I. Very low-mass planets around HD 20794, HD 85512, and HD 192310",
                    "authors": "Pepe, F.; Lovis, C.; Ségransan, D.; Benz, W.; Bouchy, F.; Dumusque, X.; Mayor, M.; Queloz, D.; Santos, N. C.; Udry, S.",
                    "journal": "Astronomy & Astrophysics",
                    "abstract": "Context. In 2009 we started an intense radial-velocity monitoring of a few nearby, slowly-rotating...",
                    "stars": [
                        {"id": 2, "name": "HIP 64690"}
                    ],
                    "planets": []
                }
            ],
            "page": 1,
            "total_pages": 1
        }
    return render_template('tables.html', data=data, title="PUBLICATIONS")
@app.route('/publications/<variable>')
def publication(variable):
    """ Returns page for single publication """
    data = {
            "id": 1,
            "ref": "2013A&A...566A.126A",
            "title": "A dynamically-packed planetary system around GJ 667C with three super-Earths in its habitable zone",
            "authors": "Anglada-Escudé, Guillem; Tuomi, Mikko; Gerlach, Enrico; Barnes, Rory",
            "journal": "Astronomy & Astrophysics",
            "abstract": "Context. Since low-mass stars have low luminosities, orbits...",
            "stars": [
                {"id": 1, "name": "Kepler-9"}
            ],
            "planets": [
                {"id": 1, "name": "Kepler-9b"},
                {"id": 2, "name": "Kepler-9c"},
                {"id": 3, "name": "Kepler-9d"}
            ]
        }
    return render_template('detail.html', data=data)

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
    except Exception: #pylint:disable=broad-except
        traceback.print_exc()
        return 'Database is not ok. Check stdout for details'


def get_commits():
    """ gets number of commits for each team member """
    url = 'https://api.github.com/repos/cs373gc-fall-2016/interswellar/stats/contributors?client_id=a857dda6c0869d2bc306&client_secret=e6f54c0cca99ebb7d6bfd5542052ed49638362ea'
    response = requests.get(url).text
    parsed = json.loads(response)
    return {user['author']['login'] : user['total'] for user in parsed}


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
