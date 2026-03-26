from mpi4py import MPI

comm = MPI.COMM_WORLD   # communicator (all processes)
rank = comm.Get_rank()  # process ID
size = comm.Get_size()  # total number of processes

print(f"Hello from rank {rank} out of {size}")

"""
Running this with: "mpirun --allow-run-as-root -n 6 $(which python) mpi_ranks.py" (I know it's not optimal, but need to finish the assignment)
Gives:
Hello from rank 2 out of 6
Hello from rank 5 out of 6
Hello from rank 0 out of 6
Hello from rank 1 out of 6
Hello from rank 4 out of 6
Hello from rank 3 out of 6
"""