
"""Advent of Code 2021 Day 1."""

# Import necessary libraries
import time
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view as swv


# Part 1 function
def p1(filename):
    """
    Return the number of increasing depths.

    Parameters
    ----------
    filename : str
        The input filename of the data.

    Returns
    -------
    count : int
        Number of increasing instances.
    """
    # Read in data
    data = np.genfromtxt(filename, dtype="int")

    # Return
    return sum(np.diff(data)>0)


# Part 2 function
def p2(filename):
    """
    Return the number of increasing depths from moving filter of size 3.

    Parameters
    ----------
    filename : str
        The input filename of the data.

    Returns
    -------
    count : int
        Number of increasing instances.
    """
    # Read in data
    data = np.genfromtxt(filename, dtype="int")

    # Create moving window
    data = np.sum(swv(data, 3), axis=-1)

    return sum(np.diff(data)>0)


if __name__ == "__main__":

    # Time tester
    start_time = time.time()
    out = p1("2021/day_1/input.csv")
    print(f"Part 1 Answer: {out}\nPart 1 Time: {time.time() - start_time} s")

    start_time = time.time()
    out = p2("2021/day_1/input.csv")
    print(f"Part 2 Answer: {out}\nPart 2 Time: {time.time() - start_time} s")
