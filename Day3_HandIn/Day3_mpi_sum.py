from mpi4py import MPI
import os


comm = MPI.COMM_WORLD   # communicator (all processes)
rank = comm.Get_rank()  # process ID
size = comm.Get_size()  # total number of processes
current_rank = rank

print(f"Hello from rank {rank} out of {size}")

total = comm.reduce(current_rank,      # Collect and sum current_rank from all processes.
            op=MPI.SUM, root=0)

if rank == 0:
    print(f'The result from the process with rank {rank} (which is the sum of ranks) = {total}')

#comm.Disconnect()
"""
Running this with: "mpirun --allow-run-as-root -n 6 $(which python) mpi_sum.py" (I know it's not optimal, but need to finish the assignment)
Gives:
Hello from rank 3 out of 6
Hello from rank 0 out of 6
Hello from rank 4 out of 6
Hello from rank 1 out of 6
Hello from rank 2 out of 6
Hello from rank 5 out of 6
The result from the process with rank 0 (which is the sum of ranks) = 15
"""