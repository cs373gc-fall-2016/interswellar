""" This module runs unittests in a python script """

import unittest
from io import StringIO

from interswellar.views_test import ViewsTest
from interswellar.models_test import ModelsTest
from interswellar.api_test import APITest


def run_tests():
    ''' Run the unittests '''
    output = StringIO()
    tests = unittest.TestSuite()
    tests.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(ViewsTest))
    tests.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(ModelsTest))
    tests.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(APITest))
    runner = unittest.TextTestRunner(stream=output, verbosity=11)
    runner.run(tests)
    return output.getvalue()
