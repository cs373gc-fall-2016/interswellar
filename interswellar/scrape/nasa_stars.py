""" Read star data from exoplanet archive """

import requests

import interswellar.scrape.lib as lib


def scrape():
    """ Read star data from exoplanet archive """

    url = 'http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?' \
          'table=mission_exocat&select=star_name,st_mass,st_lbol,st_teff,st_rad&' \
          'order=dec&format=json'

    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()

    for row in data:
        lib.create_or_update_star(
            name=row['star_name'],
            mass=row['st_mass'],
            luminosity=row['st_lbol'],
            temperature=row['st_teff'],
            radius=row['st_rad']
        )

    lib.commit()
