import time
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 1:
        messagedata = str(time.time())
        comm.send(messageData, dest=0)

if rank == 0:
        msg = comm.recv(source=1)
        print("The time was "ù + msg)

