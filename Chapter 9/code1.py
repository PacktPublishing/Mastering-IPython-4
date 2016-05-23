"""
This is an abbreviated version of my random number generator test suite.

It uses the pytest framework.  It does not do much in this form.
"""

import numpy as np
import scipy.stats
import random

class TestRandoms( ):
    """
    This is the main class.

    Normally it would hold all the tests, plus and setup and teardown fixtures.
    """
    def test_builtin(self):
        """
        Test the built-in random number generator on 10000 numbers.
        """
        num_tests = 10000
        vals = [0 for i in range(10)]
        for i in range(num_tests):
            tmp = random.randint(0, 9)
            vals[tmp] = vals[tmp] + 1

        chi2, p = scipy.stats.chisquare(self.vals)
        assert p > 0.05

def foo( ):
    """ I just needed a function outside of a class as an example"""
    pass
