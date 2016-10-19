import unittest

from interswellar import db
import interswellar.models as models


class ModelsTest(unittest.TestCase):

    """ Tests the models """

    def test_stars(self):
        star = models.Star(
            id=1, name="sun", mass=1, luminosity=1.0, temperature=1.0, radius=1.0)
        self.assertEqual(star.id, 1)
