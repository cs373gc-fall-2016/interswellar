""" Helper functions for scraping data and adding it to the database """

from interswellar import db, load_config
from interswellar.models import Star, Exoplanet, Constellation, Publication

load_config('dev')


def get_star(name):
    """ Gets a star by name from the db"""
    return Star.query.filter_by(name=name).first()


def create_or_update_star(**kwargs):
    """ Create/Update a star (if there is not star with that name) in the db"""
    star = Star.query.filter_by(name=kwargs['name']).first()
    if not star:
        star = Star(**kwargs)
        db.session.add(star)
        print("DEBUG: CREATE %s" % repr(star))
    else:
        update(star, **kwargs)
        print("DEBUG: UPDATE %s" % repr(star))

    return star


def get_planet(name):
    """ Gets an exoplanet by name from the db"""
    return Exoplanet.query.filter_by(name=name).first()


def create_or_update_planet(**kwargs):
    """ Create/Update an exoplanet (if there is not exoplanet with that name)
        in the db
    """
    planet = Exoplanet.query.filter_by(name=kwargs['name']).first()
    if not planet:
        planet = Exoplanet(**kwargs)
        db.session.add(planet)
        print("DEBUG: CREATE %s" % repr(planet))
    else:
        update(planet, **kwargs)
        print("DEBUG: UPDATE %s" % repr(planet))

    return planet


def get_constellation(name):
    """ Gets a constellation by name from the db"""
    return Constellation.query.filter_by(name=name).first()


def create_or_update_constellation(**kwargs):
    """ Create/Update a constellation (if there is not constellation with that name) in
        the db
    """
    constel = Constellation.query.filter_by(name=kwargs['name']).first()
    if not constel:
        constel = Constellation(**kwargs)
        db.session.add(constel)
        print("DEBUG: CREATE %s" % repr(constel))
    else:
        update(constel, **kwargs)
        print("DEBUG: UPDATE %s" % repr(constel))

    return constel


def get_publication(ref):
    """ Gets a publication by ref from the db"""
    return Publication.query.filter_by(ref=ref).first()


def create_or_update_publication(**kwargs):
    """ Create/Update a publication (if there is not publication with that ref) in the
        db
    """
    pub = Publication.query.filter_by(ref=kwargs['ref']).first()
    if not pub:
        pub = Publication(**kwargs)
        db.session.add(pub)
        print("DEBUG: CREATE %s" % repr(pub))
    else:
        update(pub, **kwargs)
        print("DEBUG: UPDATE %s" % repr(pub))

    return pub


def commit():
    """ Commits all scraper changes to the db """
    db.session.commit()


def update(model, **values):
    """ Updates a model with values from a dict """
    for key in values:
        setattr(model, key, values[key])
