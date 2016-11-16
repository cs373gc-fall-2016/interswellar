'''API routes for interswellar'''

import math

from flask import Blueprint, jsonify, request
from flask_restless import APIManager

import interswellar.models as models

#pylint:disable=invalid-name
public_api = Blueprint('public_api', __name__)


@public_api.route('/api/v1/search/')
def search():
    """ Run the search request and return jsonified results """
    page = int(request.args.get('page', '1'))
    # and_mode = request.args.get('mode') == 'and'
    # terms = request.args.get('q').split()

    # Do a search
    results = [
        models.Star.query.get(9),
        models.Star.query.get(10),
        models.Constellation.query.get(189),
        models.Publication.query.get(100),
        models.Exoplanet.query.get(50),
    ]

    total_pages = int(math.ceil(len(results) / 10))
    if page > total_pages:
        return "ur bad"

    # Return a json
    return jsonify({
        "page" : page,
        "total_pages" : total_pages,
        "num_results": len(results),
        "results" : [r.search_result() for r in results[10*(page-1):10*(page)]]
        })

def bind_api(app):
    """ Bind the api to the app """
    api = APIManager(app, flask_sqlalchemy_db=models.db)

    api.create_api(
        models.Star,
        collection_name='stars',
        url_prefix='/api/v1',
        include_columns=[
            'id',
            'name',
            'mass',
            'luminosity',
            'temperature',
            'radius',
            'exoplanets',
            'exoplanets.id',
            'exoplanets.name',
            'constellation',
            'constellation.id',
            'constellation.name',
            'discovered_by',
            'discovered_by.id',
            'discovered_by.ref',
        ]
    )

    api.create_api(
        models.Exoplanet,
        collection_name='exoplanets',
        url_prefix='/api/v1',
        include_columns=[
            'id',
            'name',
            'mass',
            'radius',
            'orbital_period',
            'year_discovered',
            'star',
            'star.id',
            'star.name',
            'star.constellation'
            'star.constellation.id',
            'star.constellation.abbrev',
            'discovered_by',
            'discovered_by.id',
            'discovered_by.ref',
        ]
    )

    api.create_api(
        models.Constellation,
        collection_name='constellations',
        url_prefix='/api/v1',
        include_columns=[
            'id',
            'abbrev',
            'name',
            'family',
            'meaning',
            'area',
            'stars',
            'stars.id',
            'stars.name',
            'stars.exoplanets',
            'stars.exoplanets.id',
            'stars.exoplanets.name',
        ]
    )

    api.create_api(
        models.Publication,
        collection_name='publications',
        url_prefix='/api/v1',
        include_columns=[
            'id',
            'ref',
            'title',
            'authors',
            'journal',
            'abstract',
            'year',
            'stars',
            'stars.id',
            'stars.name',
            'exoplanets',
            'exoplanets.id',
            'exoplanets.name',
        ]
    )

    app.register_blueprint(public_api)
