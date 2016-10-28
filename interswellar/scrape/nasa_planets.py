""" Read planet data from exoplanet archive """

import json
import re

import interswellar.scrape.lib as lib


def scrape():
    """ Read planet data from exoplanet archive. JK the response isn't even json wtf """
    with open('temp.json') as data_file:
        data = json.load(data_file)

    for row in data:
        star = lib.create_or_update_star(
            name=row['mpl_hostname'],
            mass=row['mst_mass'],
            luminosity=row['mst_lum'],
            temperature=row['mst_teff'],
            radius=row['mst_rad'],
        )

        try:
            pub = lib.create_or_update_publication(
                ref=extract_ref(row['mpl_reflink'])
            )
        except ValueError as err:
            print("WARN:  %s" % str(err))
        lib.create_or_update_planet(
            name=row['mpl_name'],
            mass=row['mpl_bmasse'],
            radius=row['mpl_rade'],
            orbital_period=row['mpl_orbper'],
            year_discovered=row['mpl_disc'],
            star=star,
            discovered_by=pub,
        )

    lib.commit()


def extract_ref(link):
    """ Extracts a reference from an a tag pointing to harvard absads """
    patterns = [
        re.compile(r'<a href=http://adsabs.harvard.edu/cgi-bin/nph-bib_query\?'
                   r'bibcode=([^\s]*)(\s+.*)?>.*</a>'),
        re.compile(r'<a href=http://adsabs.harvard.edu/abs/([^\s]*)'
                   r'(\s+.*)?>.*</a>'),
    ]
    for pattern in patterns:
        match = pattern.search(link)
        if match:
            return match.group(1)

    raise ValueError("%s does not look like a absads.harvard.edu link" % link)
