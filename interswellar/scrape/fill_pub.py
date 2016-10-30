""" Scrape publication data from absads """

import requests
import ads


import interswellar.scrape.lib as lib
from interswellar.models import Publication

def scrape():
    for pub in Publication.query.filter(Publication.title == None).all():
        try:
            resp = ads.SearchQuery(q=pub.ref, fl=[
                'title', 'year', 'author', 'pub', 'abstract'
            ])
            data = list(resp)
        except Exception as err:
            print("WARN: Bad response from server for %s: %s" % (pub.ref, str(err)))
            continue


        if not data:
            print("WARN: Could not find data for %s" % pub.ref)
            continue

        paper = data[0]

        lib.create_or_update_publication(
            ref=pub.ref,
            title=paper.title[0],
            year=int(paper.year),
            authors='; '.join(paper.author),
            journal=paper.pub,
            abstract=paper.abstract,
        )

        remaining = resp.response.get_ratelimits()['remaining'];
        if int(remaining) < 50:
            print("WARN: Only %d requests remaining, terminating", remaining)
            break;

    lib.commit()