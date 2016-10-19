"""models for database"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

BASE = declarative_base()

# pylint: disable=too-few-public-methods
class Star(BASE):
    """model for stars"""
    __tablename__ = 'stars'

    # pylint: disable=invalid-name
    id = Column(Integer, primary_key=True)
    name = Column(String)
    mass = Column(Float)
    luminosity = Column(Float)
    temperature = Column(Float)
    radius = Column(Float)
    exoplanets = relationship("Exoplanet", back_populates="star")
    # constellation, publication discovered

    def __repr__(self):
        return "<Star(name='%s', mass=%f, luminosity=%f, temperature=%f, radius=%f)>" % (
            self.name, self.mass, self.luminosity, self.temperature, self.radius)

# pylint: disable=too-few-public-methods
class Exoplanet(BASE):
    """model for exoplanets"""
    __tablename__ = 'exoplanets'

    # pylint: disable=invalid-name
    id = Column(Integer, primary_key=True)
    name = Column(String)
    mass = Column(Float)
    radius = Column(Float)
    orbital_period = Column(Integer)
    year_discovered = Column(Integer)
    star_id = Column(Integer, ForeignKey("star.id"))
    star = relationship("Star", back_populates="exoplanets")
    # constellation, publication discovered

    def __repr__(self):
        return "<Exoplanet(name='%s', mass=%f, radius=%f, orbital_period=%d, "  \
            "year_discovered=%d)>" % (self.name, self.mass, self.radius,
                                      self.orbital_period, self.year_discovered)
