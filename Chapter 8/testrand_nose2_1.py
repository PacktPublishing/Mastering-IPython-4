import numpy as np
import myrand
import scipy.stats
import sys
import random

numVals = 0
vals = 0
randGen = 0

def setup():
    print("Doing setUp")
    global numVals
    global vals
    global randGen
    numVals = 10000
    vals = np.zeros((10), dtype=np.int32)
    randGen = myrand.MyRand( )

def test_bad():
    print("Doing test_bad")
    x0 = 15
    p1 = 50
    p2 = 100
    modulus = 2217
    randGen.set(p1, p2, x0, modulus)
    for i in range(numVals):
        tmp = randGen.next( )
        tmp = tmp % 10
        vals[tmp] = vals[tmp] + 1

    chi2, p = scipy.stats.chisquare(vals)
    assert p > 0.05
    
def test_better():
    print("Doing test_better")
    x0 = 79
    p1 = 263
    p2 = 71
    modulus = sys.maxsize
    randGen.set(p1, p2, x0, modulus)
    for i in range(numVals):
        tmp = randGen.next( )
        tmp = tmp % 10
        vals[tmp] = vals[tmp] + 1

    chi2, p = scipy.stats.chisquare(vals)
    assert p > 0.05

def test_builtin():
    print("Doing test_builtin")
    for i in range(numVals):
        tmp = random.randint(0, 9)
        vals[tmp] = vals[tmp] + 1

    chi2, p = scipy.stats.chisquare(vals)
    assert p > 0.05

def teardown():
    print("Doing tearDown")
    randGen.reset( )

test_bad.setup = setup
test_bad.teardown = teardown
test_better.setup = setup
test_better.teardown = teardown
test_builtin.setup = setup
test_builtin.teardown = teardown
