"""models for database"""

from interswellar import db

# pylint: disable=too-few-public-methods


class Star(db.Model):

    """model for stars"""
    __tablename__ = 'stars'

    # pylint: disable=invalid-name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    mass = db.Column(db.Float)
    luminosity = db.Column(db.Float)
    temperature = db.Column(db.Float)
    radius = db.Column(db.Float)
    exoplanets = db.relationship("Exoplanet", backref="star")
    constellation_id = db.Column(
        db.Integer, db.ForeignKey("constellations.id"))
    publication_id = db.Column(db.Integer, db.ForeignKey("publications.id"))

    def __repr__(self):
        return "<Star(name='%s', mass=%f, luminosity=%f, temperature=%f, radius=%f)>" % (
            self.name, self.mass, self.luminosity, self.temperature, self.radius)

# pylint: disable=too-few-public-methods


class Exoplanet(db.Model):

    """model for exoplanets"""
    __tablename__ = 'exoplanets'

    # pylint: disable=invalid-name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    mass = db.Column(db.Float)
    radius = db.Column(db.Float)
    orbital_period = db.Column(db.Integer)
    year_discovered = db.Column(db.Integer)
    star_id = db.Column(db.Integer, db.ForeignKey("stars.id"))
    publication_id = db.Column(db.Integer, db.ForeignKey("publications.id"))

    def __repr__(self):
        return "<Exoplanet(name='%s', mass=%f, radius=%f, orbital_period=%d, "  \
            "year_discovered=%d)>" % (self.name, self.mass, self.radius,
                                      self.orbital_period, self.year_discovered)

# pylint: disable=too-few-public-methods


class Constellation(db.Model):

    """model for constellations"""
    __tablename__ = 'constellations'

    # pylint: disable=invalid-name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    abbrev = db.Column(db.String)
    family = db.Column(db.String)
    meaning = db.Column(db.String)
    area = db.Column(db.Float)
    stars = db.relationship("Star", backref="constellation")
    # bordering constellations

    def __repr__(self):
        return "<Constellation(name='%s', abbrev='%s', family='%s', "  \
            "meaning='%s', area='%s')>" % (self.name, self.abbrev,
                                           self.family, self.meaning, self.area)

# pylint: disable=too-few-public-methods


class Publication(db.Model):

    """model for publication"""
    __tablename__ = 'publications'

    # pylint: disable=invalid-name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    year = db.Column(db.Integer)
    authors = db.Column(db.String)
    journal = db.Column(db.String)
    abstract = db.Column(db.String)
    stars = db.relationship("Star", backref="publication")
    exoplanets = db.relationship("Exoplanet", backref="publication")

    def __repr__(self):
        return "<Publication(name='%s', year=%f, authors='%s', journal='%s', abstract='%s')>" % (
            self.name, self.year, self.authors, self.journal, self.abstract)