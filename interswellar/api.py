'''API routes for interswellar'''

from interswellar import apimanager
import interswellar.models as models

apimanager.create_api(
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
        'publication',
        'publication.id',
        'publication.name',
    ]
)
