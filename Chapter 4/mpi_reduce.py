import numpy
import sys
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# integrate from in [0, 4] using 8 rectangles
a = 0
b = 4
n = 8

# the function to integrate
def f(x):
        return x*x*x

# use the left-most point in the range as the height
def calcArea(lft, dx):
        ht = f(lft)
        return ht * dx

# use regular intervals
dx = (b-a)/n

# local_a is the leftmost point
local_a = rank * dx

# initializing variables
# when using capital-R Recv, mpi4py requires that we pass buffer-like
# objects, so why not use numpy?
integral = numpy.zeros(1)
total = numpy.zeros(1)

# perform local computation
integral[0] = calcArea(local_a, dx)

# communication
# root node receives results with a collective "reduce"
comm.Reduce(integral, total, op=MPI.SUM, root=0)

# root process prints results
if comm.rank == 0:
        print("With n =", n, "trapezoids, our estimate of the integral from", a, "to", b, "is", total)

