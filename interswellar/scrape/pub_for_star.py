""" Find publications for stars in the db """

import StringIO
import requests

import interswellar.scrape.lib as lib
from interswellar.models import Star, Publication

def scrape():
    """ Find publications for stars in the db """
    for star in Star.query.all():
        if star.discovered_by is None:
            url = 'http://simbad.u-strasbg.fr/simbad/sim-id?output.format=ascii&Ident=%s' %
                star.name
            resp = requests.get(url)
            if(resp.status_code != requests.codes.ok):
                print("WARN: Looking up %s in SIMBAD failed: status %d" % 
                    (star.name, resp.status_code))

            data = iter(StringIO(resp.text))
            while not next(data).startsWith('Bibcodes'):
                pass

            codes = []
            for line in data:
                if not line.strip():
                    break;

                codes += line.strip().split()

            pub = lib.create_or_update_publication(
                ref = next(code in reversed(codes) if code.startsWith('2'))
            )

            star.discovered_by = pub


    lib.commit()
