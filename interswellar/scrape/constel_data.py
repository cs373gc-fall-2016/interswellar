""" Read constellation data from wikipedia """

import re
import requests

import interswellar.scrape.lib as lib


def scrape():
    """ Read constellation data from wikipedia """

    clist = get_wiki('88_modern_constellations')

    for line in clist:
        if line.startswith('{| class="wikitable sortable"'):
            break

    for i in range(6):  # Skip lines
        next(clist)

    name_regex = re.compile(r'^\| \[\[(.*\|)?([\w ]+)\]\]')
    area_regex = re.compile(r'^\| areatotal = (\d+)')
    for line in clist:
        if not line:
            break
        args = line.split('||')

        match = name_regex.search(args[0])
        name = match.group(2)
        link = match.group(1)[:-1] if match.group(1) else name
        abbrev = args[1].strip()
        family = args[4].strip()
        meaning = re.sub(
            r"\[\[(.*\|)?([\w()' ]+)\]\]", '\g<2>', args[6].strip())

        cpage = get_wiki(link)
        for line in cpage:
            match = area_regex.search(line)
            if match:
                area = float(match.group(1))
                break

        lib.create_or_update_constellation(
            name=name,
            abbrev=abbrev,
            family=family,
            meaning=meaning,
            area=area,
        )

        next(clist)  # Skip a line

    lib.commit()


def get_wiki(title):
    url = 'https://en.wikipedia.org/w/api.php?action=query' \
          '&format=json&prop=revisions&rvprop=content&' \
          'titles=%s' % title

    resp = requests.get(url)
    resp.raise_for_status()
    content = next(iter(resp.json()['query']['pages'].values()))
    return iter(content['revisions'][0]['*'].splitlines())
