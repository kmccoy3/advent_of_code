
# Import necessary libraries
import numpy as np
import pandas as pd
from itertools import permutations as perms
import time

# Read in puzzle input
data = pd.read_csv('input.csv', header=None).values


# Part 1 function
def p1():
    for p in perms(data, 2):
        if sum(p) == 2020:
            return np.prod(p)


# Part 2 function
def p2():
    for p in perms(data, 3):
        if sum(p) == 2020:
            return np.prod(p)


# Time tester
start_time = time.time()
out = p2()
print("My program took", time.time() - start_time, "seconds to run.")
