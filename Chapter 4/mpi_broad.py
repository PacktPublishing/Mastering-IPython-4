from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
   data = input(“Please enter random number seed”)
else:
   data = None

# mpi4py wants to send an object, so we will leave the input in that format
data = comm.bcast(data, root=0)

