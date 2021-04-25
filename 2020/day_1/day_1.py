
# Import necessary libraries
import numpy as np
from itertools import combinations as combs
import time

# Read in puzzle input
data = np.genfromtxt("input.csv", dtype="int")  # way faster than pandas df


# Part 1 function
def p1():
    for p in combs(data, 2):
        if sum(p) == 2020:
            return np.prod(p)


# Part 2 function
def p2():
    for p in combs(data, 3):
        if sum(p) == 2020:
            return np.prod(p)


# Time tester
start_time = time.time()
out = p2()
print("My program took", time.time() - start_time, "seconds to run.")
