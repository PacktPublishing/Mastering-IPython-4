import unittest
import numpy as np
import myrand
import scipy.stats
import sys
import random

class TestRandoms(unittest.TestCase):

    def setUp(self):
        print("Doing setUp")
        self.numVals = 10000
        self.vals = np.zeros((10), dtype=np.int32)
        self.randGen = myrand.MyRand( )

    def test_bad(self):
        print("Doing test_bad")
        x0 = 15
        p1 = 50
        p2 = 100
        modulus = 2217
        self.randGen.set(p1, p2, x0, modulus)
        for i in range(self.numVals):
            tmp = self.randGen.next( )
            tmp = tmp % 10
            self.vals[tmp] = self.vals[tmp] + 1

        chi2, p = scipy.stats.chisquare(self.vals)
        self.assertGreater(p, 0.05)
        
    def test_better(self):
        print("Doing test_better")
        x0 = 79
        p1 = 263
        p2 = 71
        modulus = sys.maxsize
        self.randGen.set(p1, p2, x0, modulus)
        for i in range(self.numVals):
            tmp = self.randGen.next( )
            tmp = tmp % 10
            self.vals[tmp] = self.vals[tmp] + 1

        chi2, p = scipy.stats.chisquare(self.vals)
        self.assertGreater(p, 0.05)

    def test_builtin(self):
        print("Doing test_builtin")
        for i in range(self.numVals):
            tmp = random.randint(0, 9)
            self.vals[tmp] = self.vals[tmp] + 1

        chi2, p = scipy.stats.chisquare(self.vals)
        self.assertGreater(p, 0.05)


    def tearDown(self):
        print("Doing tearDown")
        self.randGen.reset( )
            

if __name__ == '__main__':
    unittest.main()
