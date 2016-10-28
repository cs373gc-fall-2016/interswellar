""" Find publications for stars in the db """
import io
import requests

import interswellar.scrape.lib as lib
from interswellar.models import Star


def scrape():
    """ Find publications for stars in the db """
    for star in Star.query.all():
        if star.discovered_by is None:
            name = star.name.replace('+', '%2b')
            codes = []
            candidates = [
                name,
                ' '.join(name.split()[:-1]),
                name.replace(' ', '-'),
                '-'.join(name.split()[:-1]),
                name[:-1] + '-' + name[-1],
            ]
            for candidate in candidates:
                try:
                    codes = simbad_lookup(candidate)
                except ValueError as err:
                    print('DEBUG: %s' % str(err))

                if codes:
                    break

            if not codes:
                print('WARN: No codes found for any of %s' % str(candidates))
                continue

            pub = lib.create_or_update_publication(
                ref=next(
                    (code for code in reversed(codes) if code.startswith('2')))
            )

            lib.create_or_update_star(
                name=star.name,
                discovered_by=pub,
            )

    lib.commit()


def simbad_lookup(name):
    """ Lookup bibcodes from simbad """

    url = 'http://simbad.u-strasbg.fr/simbad/sim-id?output.format=ascii&Ident=%s' % name
    resp = requests.get(url)
    if resp.status_code != 200:
        raise ValueError("Looking up %s in SIMBAD failed: status %d" %
                         (name, resp.status_code))

    data = iter(io.StringIO(resp.text))

    for line in data:
        if line.startswith('!! Identifier not found'):
            raise ValueError('Identifier not found in SIMBAD: %s' % url)
        if line.startswith('Number of objects:'):
            raise ValueError('Name provided is a category: %s' % url)
        if line.startswith('Bibcodes'):
            break

    codes = []
    for line in data:
        if not line.strip():
            break

        codes += line.strip().split()

    return codes
