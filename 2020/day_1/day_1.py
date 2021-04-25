
"""Advent of Code 2020 Day 1."""

# Import necessary libraries
import numpy as np
from itertools import combinations as combs
import time


# Part 1 function
def p1(filename):
    """
    Return the product of two numbers that add to 2020.

    Parameters
    ----------
    filename : str
        The input filename of the data.

    Returns
    -------
    count : int
        Product of the two numbers that ads to 2020.

    """
    # Read in data
    data = np.genfromtxt(filename, dtype="int")

    # Loop through all combinations of numbers, test if sum is 2020
    for p in combs(data, 2):
        if sum(p) == 2020:
            return np.prod(p)


# Part 2 function
def p2(filename):
    """
    Return the product of three numbers that add to 2020.

    Parameters
    ----------
    filename : str
        The input filename of the data.

    Returns
    -------
    count : int
        Product of the three numbers that ads to 2020.

    """
    # Read in data
    data = np.genfromtxt(filename, dtype="int")

    # Loop through all combinations of numbers, test if sum is 2020
    for p in combs(data, 3):
        if sum(p) == 2020:
            return np.prod(p)


# Time tester
start_time = time.time()
out = p1("input.csv")
print("Part 1 took", time.time() - start_time, "seconds to run.")

start_time = time.time()
out = p2("input.csv")
print("Part 2 took", time.time() - start_time, "seconds to run.")
