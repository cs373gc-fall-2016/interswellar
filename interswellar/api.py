'''API routes for interswellar'''

import math

from flask import Blueprint, jsonify, request
from flask_restless import APIManager
from sqlalchemy import or_, and_

import interswellar.models as models

# pylint:disable=invalid-name
public_api = Blueprint('public_api', __name__)


@public_api.route('/api/v1/search')
@public_api.route('/api/v1/search/')
def search():
    """ Run the search request and return jsonified results """
    page = int(request.args.get('page', '1'))
    and_mode = request.args.get('mode') == 'and'
    terms = request.args.get('q').split()
    if not terms:
        return "ur bad"

    op = and_ if and_mode else or_

    # Do a search
    stars = [star_filter(t) for t in terms]
    exoplanets = [exoplanet_filter(t) for t in terms]
    constellations = [constellation_filter(t) for t in terms]
    publications = [publication_filter(t) for t in terms]
    results = models.Star.query.filter(op(*stars)).all() + \
        models.Exoplanet.query.filter(op(*exoplanets)).all() + \
        models.Constellation.query.filter(op(*constellations)).all() + \
        models.Publication.query.filter(op(*publications)).all()

    total_pages = int(math.ceil(len(results) / 10))
    if page > total_pages:
        return jsonify({
            "message": "ur bad",
            "total_pages": total_pages,
            "num_results": len(results)
        })

    # Return a json
    return jsonify({
        "page": page,
        "total_pages": total_pages,
        "num_results": len(results),
        "results": [r.search_result() for r in results[10 * (page - 1):10 * (page)]]
    })


def star_filter(term):
    """Apply filter to star models"""
    return ((models.Star.id == safecast(term, int, -1)) |
            (models.Star.name.ilike('%' + term + '%')) |
            (models.Star.mass == safecast(term, float, -1.0)) |
            (models.Star.luminosity == safecast(term, float, -1.0)) |
            (models.Star.temperature == safecast(term, float, -1.0)) |
            (models.Star.radius == safecast(term, float, -1.0)))


def exoplanet_filter(term):
    """Apply filter to exoplanet models"""
    return ((models.Exoplanet.id == safecast(term, int, -1)) |
            (models.Exoplanet.name.ilike('%' + term + '%')) |
            (models.Exoplanet.mass == safecast(term, float, -1.0)) |
            (models.Exoplanet.radius == safecast(term, float, -1.0)) |
            (models.Exoplanet.orbital_period == safecast(term, int, -1)) |
            (models.Exoplanet.year_discovered == safecast(term, int, -1)))


def constellation_filter(term):
    """Apply filter to constellation models"""
    return ((models.Constellation.id == safecast(term, int, -1)) |
            (models.Constellation.name.ilike('%' + term + '%')) |
            (models.Constellation.abbrev.ilike('%' + term + '%')) |
            (models.Constellation.family.ilike('%' + term + '%')) |
            (models.Constellation.meaning.ilike('%' + term + '%')) |
            (models.Constellation.area == safecast(term, float, -1.0)))


def publication_filter(term):
    """Apply filter to publication models"""
    return ((models.Publication.id == safecast(term, int, -1)) |
            (models.Publication.ref.ilike('%' + term + '%')) |
            (models.Publication.title.ilike('%' + term + '%')) |
            (models.Publication.year == safecast(term, int, -1)) |
            (models.Publication.authors.ilike('%' + term + '%')) |
            (models.Publication.journal.ilike('%' + term + '%')) |
            (models.Publication.abstract.ilike('%' + term + '%')))


def safecast(term, typ, default):
    """Method to safely cast objects to others"""
    try:
        return typ(term)
    except (ValueError, TypeError):
        return default


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
