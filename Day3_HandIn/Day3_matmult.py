# Program to multiply two matrices using nested loops
import random
import timeit
import numpy as np
#=================================================================================================#
#   ANSWER: The printouts take forever, so commenting them out.
#           When running only N = 2 with timeit, it gives: Time taken = 4.519549042001017 s.
#           
#           After changing all the for loops to list comprehensions, I  get: Time taken = 4.561430254005245 s
#           So that actually took longer. I guess there is some overhead or intermediate switching going on behind
#           the scenes.
#
#           Double or triple for loops are always a bad idea. To multiply them we can use the numpy dot product function
#           Using that gives: Time taken = 5.5408622909963015 s.
#           So that actually slowed it down. My guess is that I am not letting it work with arrays. So the next step
#           is to convert the lists to arrays. Or better yet, create them as arrays from the start.
#
#           #---------------- N = 3 --------------------#
#           Time taken for original = 8.663842927999212
#           Time taken for numpy = 9.648282409994863
#           #---------------- N = 10 --------------------#
#           Time taken for original = 118.0223016730015
#           Time taken for numpy = 11.804670377998264
#
#           I did try to run it for large N, but the time taken for the loop script is just ridiculous.
#           I beleive this N=10 example proves the point. Contiguous, pre-acllocated arrays are much faster.
#           The initial overhead of numpy washes out the benefits for small N, but it starts to pay off already
#           at N = 10.
#
#=================================================================================================#
def day3_matmult(size=10):
    N = size

    # NxN matrix
    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])                   
    #[X.append([random.randint(0,100) for r in range(N)]) for i in range(N)]    Slower

    # Nx(N+1) matrix
    Y = []
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])                  
    #[Y.append([random.randint(0,100) for r in range(N+1)]) for i in range(N)]  Slower
   
    # result is Nx(N+1)
    result = []
    for i in range(N):
        result.append([0] * (N+1))                                   
    #[result.append([0] * (N+1)) for i in range(N)]                             Slower
    
    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    #for r in result:
    #    print(r)
    #-------------------------------------------------------------------------------------#

def day3_matmult_numpy(size=10):
    N = size
    X = np.random.randint(low=0, high=100, size=(N,N))
    Y = np.random.randint(low=0, high=100, size=(N,N))
    result = np.zeros((N,N+1))
    result = np.dot(X,Y)
    #for r in result:
    #    print(r)


print(f'Time taken for original = {timeit.timeit(day3_matmult)}')
print(f'Time taken for numpy = {timeit.timeit(day3_matmult_numpy)}')
