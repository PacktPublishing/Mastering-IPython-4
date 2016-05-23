import numpy as np
import myrand
import scipy.stats
import sys
import random
import nose2.tools.decorators

#class TestRandoms( ):

    #def __init__(self):
        #self.test_bad.setup = self.setup
        #self.test_bad.teardown = self.teardown


def setup():
    print("Doing setUp")
#    self.numVals = 10000
#    self.vals = np.zeros((10), dtype=np.int32)
#    self.randGen = myrand.MyRand( )

def teardown():
    print("Doing tearDown")
#        x = 1/0
#        self.randGen.reset( )

@nose2.tools.decorators.with_setup(teardown)
def test_bad():
    print("Doing test_bad")
#        x0 = 15
#        p1 = 50
#        p2 = 100
#        modulus = 2217
#        self.randGen.set(p1, p2, x0, modulus)
#        for i in range(self.numVals):
#            tmp = self.randGen.next( )
#            tmp = tmp % 10
#            self.vals[tmp] = self.vals[tmp] + 1

#        chi2, p = scipy.stats.chisquare(self.vals)
#        assert p > 0.05
        
def test_better():
    print("Doing test_better")
#        x0 = 79
#        p1 = 263
#        p2 = 71
#        modulus = sys.maxsize
#        self.randGen.set(p1, p2, x0, modulus)
#        for i in range(self.numVals):
#            tmp = self.randGen.next( )
#            tmp = tmp % 10
#            self.vals[tmp] = self.vals[tmp] + 1

#        chi2, p = scipy.stats.chisquare(self.vals)
#        assert p > 0.05

def test_builtin():
    print("Doing test_builtin")
#        for i in range(self.numVals):
#            tmp = random.randint(0, 9)
#            self.vals[tmp] = self.vals[tmp] + 1

#        chi2, p = scipy.stats.chisquare(self.vals)
#        assert p > 0.05

test_bad.setup = setup

