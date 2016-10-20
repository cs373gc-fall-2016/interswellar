'''API routes for interswellar'''

from interswellar import apimanager
import interswellar.models as models

API_KWARGS = {
    "url_prefix": "/api/v1"
}

apimanager.create_api(
    models.Star,
    collection_name='stars',
    include_columns=[
        'id',
        'name',
        'mass',
        'luminosity',
        'temperature',
        'radius',
        'exoplanets.id',
        'exoplantes.name',
        'constellation.id',
        'constellation.name',
        'publication.id',
        'publication.name',
    ],
    **API_KWARGS
)
