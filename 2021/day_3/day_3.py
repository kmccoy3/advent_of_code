
"""Advent of Code 2021 Day 3."""

# Import necessary libraries
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view as swv
import time


# Part 1 function
def p1(filename):
    """
    Return the power consumption of the submarine.

    Parameters
    ----------
    filename : str
        The input filename of the data.

    Returns
    -------
    pow : int
        Power consumption of the submarine.
    """

    # Read in data
    data = np.genfromtxt(filename, dtype="int", delimiter=1)

    rows, _ = data.shape

    data = np.sum(data, axis=0) / rows

    data = np.around(data)

    gamma = ""
    epsilon = ""
    for num in data:
        gamma = gamma + str(int(num))
        epsilon = epsilon + str(1 - int(num))

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    return gamma * epsilon


# Part 2 function
def p2(filename):
    """
    Return the life support rating of the submarine.

    Parameters
    ----------
    filename : str
        The input filename of the data.

    Returns
    -------
    lsp : int
        Life support rating of the submarine.
    """

    # Read in data
    data = np.genfromtxt(filename, dtype="int", delimiter=1)

    oxy_data = np.copy(data)
    co2_data = np.copy(data)


    oxy = ""
    co2 = ""


    rows, cols = oxy_data.shape
    for i in range(cols):
        num_ones = sum(oxy_data[:, i])
        if num_ones >= rows/2:
            oxy_data = oxy_data[oxy_data[:, i] == 1, :]
            oxy = oxy + "1"
        elif num_ones < rows/2:
            oxy_data = oxy_data[oxy_data[:, i] == 0, :]
            oxy = oxy + "0"
        rows, cols = oxy_data.shape
        if rows == 1:
            oxy = ""
            for num in oxy_data[0, :]:
                oxy = oxy + str(int(num))
            break


    rows, cols = co2_data.shape
    for i in range(cols):
        num_ones = sum(co2_data[:, i])
        if num_ones < rows/2:
            co2_data = co2_data[co2_data[:, i] == 1]
            co2 = co2 + "1"
        elif num_ones >= rows/2:
            co2_data = co2_data[co2_data[:, i] == 0]
            co2 = co2 + "0"
        rows, cols = co2_data.shape
        if rows == 1:
            co2 = ""
            for num in co2_data[0, :]:
                co2 = co2 + str(int(num))
            break


    oxy = int(oxy, 2)
    co2 = int(co2, 2)

    return oxy * co2


if __name__ == "__main__":

    # Time tester
    start_time = time.time()
    out = p1("2021/day_3/input.txt")
    print(f"Part 1 Answer: {out}\nPart 1 Time: {time.time() - start_time} s")

    start_time = time.time()
    out = p2("2021/day_3/input.txt")
    print(f"Part 2 Answer: {out}\nPart 2 Time: {time.time() - start_time} s")
