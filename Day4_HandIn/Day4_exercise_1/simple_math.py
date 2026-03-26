import numpy as np

def simple_math(num_of_ints):
    """ Function to compute the sum of the 'num' first integers"""
    tot_sum = 0
    numbers = np.arange(1,num_of_ints+1,1)
    for integer in numbers:
        tot_sum += integer
    return tot_sum
    


