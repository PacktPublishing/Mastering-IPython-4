"""
This is my hailstone unit test suite.

It uses the unittest framework.  Admittedly, it does not do much.
"""

import unittest
from hail1 import f

class TestHailStones(unittest.TestCase):
    """
    The main class for testing the hailstone sequence generator.
    """

    def test_f(self):
        """currently the only test in this suite."""
        ans = [0, 0, 1, 7, 2, 5, 8, 16, 3, 19, 6]
        for i in range(1, 11):
            print(i)
            self.assertEqual(f(i), ans[i])

def foo( ):
    """
    An independent function.

    I needed another function to illustrate the docstring for a function that was not a member of a class.
    """
    pass