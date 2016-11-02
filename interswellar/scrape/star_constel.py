""" Find constellations for stars in the db """
from astropy.coordinates import get_constellation, get_icrs_coordinates

import interswellar.scrape.lib as lib
from interswellar.models import Star


def scrape():
    """ Find constellations for stars in the db """
    for star in Star.query.all():
        name = star.name
        candidates = [
            name,
            ' '.join(name.split()[:-1]),
            name.replace(' ', '-'),
            '-'.join(name.split()[:-1]),
            name[:-1] + '-' + name[-1],
        ]
        constellation = None
        for candidate in candidates:
            try:
                constellation = get_constellation(
                    get_icrs_coordinates(candidate)
                )
            except Exception as err:
                print('DEBUG: %s' % str(err))
            else:
                break

        if not constellation:
            print('WARN: No constellation found for star %s' % name)
            continue

        constel = lib.create_or_update_constellation(
            name=constellation
        )

        lib.create_or_update_star(
            name=star.name,
            constellation=constel
        )

    lib.commit()
