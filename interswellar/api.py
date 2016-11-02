'''API routes for interswellar'''

from flask_restless import APIManager
import interswellar.models as models


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
            'stars',
            'stars.id',
            'stars.name',
            'exoplanets',
            'exoplanets.id',
            'exoplanets.name',
        ]
    )
