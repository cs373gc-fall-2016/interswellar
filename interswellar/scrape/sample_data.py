""" Adds sample data to the database """

# pylint:disable=line-too-long

import interswellar.scrape.lib as lib


def scrape():
    """ Puts sample data in database """

    keplerpub = lib.create_or_update_publication(
        ref='2010Sci...330...51H',
        year=2010,
        title='Kepler-9: A System of Multiple Planets Transiting a Sun-Like Star, Confirmed by Timing Variations',
        authors='Holman, Matthew J.; Fabrycky, Daniel C.; Ragozzine, Darin; Ford, Eric B.; Steffen, Jason H.; Welsh, William F.; Lissauer, Jack J.; Latham, David W.; Marcy, Geoffrey W.; Walkowicz, Lucianne M.; Batalha, Natalie M.; Jenkins, Jon M.; Rowe, Jason F.; Cochran, William D.; Fressin, Francois; Torres, Guillermo; Buchhave, Lars A.; Sasselov, Dimitar D.; Borucki, William J.; Koch, David G.; Basri, Gibor; Brown, Timothy M.; Caldwell, Douglas A.; Charbonneau, David; Dunham, Edward W.; Gautier, Thomas N.; Geary, John C.; Gilliland, Ronald L.; Haas, Michael R.; Howell, Steve B.; Ciardi, David R.; Endl, Michael; Fischer, Debra; Furesz, Gabor; Hartman, Joel D.; Isaacson, Howard; Johnson, John A.; MacQueen, Phillip J.; Moorhead, Althea V.; Morehead, Robert C.; Orosz, Jerome A.',
        journal='Science',
        abstract='The Kepler spacecraft is monitoring more than 150,000 stars for evidence of planets transiting those stars. We report the detection of two Saturn-size planets that transit the same Sun-like star, based on 7 months of Kepler observations. Their 19.2- and 38.9-day periods are presently increasing and decreasing at respective average rates of 4 and 39 minutes per orbit; in addition, the transit times of the inner body display an alternating variation of smaller amplitude. These signatures are characteristic of gravitational interaction of two planets near a 2:1 orbital resonance. Six radial-velocity observations show that these two planets are the most massive objects orbiting close to the star and substantially improve the estimates of their masses. After removing the signal of the two confirmed giant planets, we identified an additional transiting super-Earth-size planet candidate with a period of 1.6 days.'
    )
    hippub = lib.create_or_update_publication(
        ref='1975MSS...C01....0H',
        year=1975,
        title='University of Michigan Catalogue of two-dimensional spectral types for the HD stars. Volume I. Declinations -90_ to -53_f0.',
        authors='Houk, N.; Cowley, A. P.',
        journal='University of Michigan Catalogue of two-dimensional spectral types for the HD stars',
        abstract='Not available'
    )
    gjpub = lib.create_or_update_publication(
        ref='2000ApJ...539..241S',
        year=2000,
        title='Nearby Microlensing Events: Identification of the Candidates for theSpace Interferometry Mission',
        authors='Salim, Samir; Gould, Andrew',
        journal='The Astrophysical Journal',
        abstract='The Space Interferometry Mission (SIM) is the instrument of choice when it comes to observing astrometric microlensing events where nearby, usually high proper motion, stars (``lenses'') pass in front of more distant stars (``sources''). Each such encounter produces a deflection in the source\'s apparent position that, when observed by SIM, can lead to a precise mass determination of the nearby lens star. We search for lens-source encounters during the 2005-2015 period using Hipparcos, ACT, and NLTT to select lenses, and USNO-A2.0 to search for the corresponding sources, and rank these by the SIM time required for a 1% mass measurement. For Hipparcos and ACT lenses, the lens distance and lens-source impact parameter are precisely determined so that the events are well characterized. We present 32 candidates beginning with a 61 Cyg A event in 2012 that requires only a few minutes of SIM time. Proxima Centauri and Barnard\'s star each generate several events. For NLTT lenses, the distance is known only to a factor of 3, and the impact parameter only to 1\'\'. Together, these produce uncertainties of a factor ~10 in the amount of SIM time required. We present a list of 146 NLTT candidates and show how single-epoch CCD photometry of the candidates could reduce the uncertainty in SIM time to a factor of ~1.5.',
    )

    # Create Constellations
    lyra = lib.create_or_update_constellation(
        abbrev='Lyr',
        name='Lyra',
        family='Hercules',
        meaning='lyre / harp',
        area=286,
    )

    octans = lib.create_or_update_constellation(
        abbrev='Oct',
        name='Octans',
        family='La Caille',
        meaning='octant (instrument)',
        area=291,
    )

    ara = lib.create_or_update_constellation(
        abbrev='Ara',
        name='Ara',
        family='Hercules',
        meaning='altar',
        area=237,
    )

    # Create stars
    kepler = lib.create_or_update_star(
        name='Kepler-9',
        luminosity=13.9,
        mass=1.07,
        radius=1.02,
        temperature=5777.00,
        constellation=lyra,
        discovered_by=keplerpub,
    )
    lib.create_or_update_star(
        name='HIP 64690',
        luminosity=0.810,
        mass=0.95,
        radius=0.93,
        temperature=5679.00,
        constellation=octans,
        discovered_by=hippub,
    )
    lib.create_or_update_star(
        name='G 674',
        luminosity=0.016,
        mass=0.35,
        radius=0.41,
        temperature=3600.00,
        constellation=ara,
        discovered_by=gjpub,
    )

    # Create planets
    lib.create_or_update_planet(
        name='Kepler-9b',
        mass=80.09,
        radius=9.438,
        orbital_period=1662336,
        year_discovered=2010,
        star=kepler,
        discovered_by=keplerpub,
    )
    lib.create_or_update_planet(
        name='Kepler-9c',
        mass=54.249,
        radius=9.225,
        orbital_period=3361824,
        year_discovered=2010,
        star=kepler,
        discovered_by=keplerpub,
    )
    lib.create_or_update_planet(
        name='Kepler-9d',
        mass=None,
        radius=1.6,
        orbital_period=137376,
        year_discovered=2010,
        star=kepler,
        discovered_by=keplerpub,
    )

    lib.commit()
