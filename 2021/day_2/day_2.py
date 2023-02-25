
"""Advent of Code 2021 Day 1."""

# Import necessary libraries
import time


# Part 1 function
def p1(filename):
    """
    Return product of the final depth and distance.

    Parameters
    ----------
    filename : str
        The input filename of the data.

    Returns
    -------
    product : int
        Product of final depth and distance.
    """

    # Initialize counters
    depth = 0
    distance = 0

    with open(filename) as f:
        for line in f:
            direction, num = line.split(" ")
            if direction == "forward":
                distance += int(num)
            elif direction == "up":
                depth -= int(num)
            elif direction == "down":
                depth += int(num)

    return depth * distance


# Part 2 function
def p2(filename):
    """
    Return product of the final depth and distance.

    Parameters
    ----------
    filename : str
        The input filename of the data.

    Returns
    -------
    product : int
        Product of final depth and distance.
    """

    # Initialize counters
    depth = 0
    distance = 0
    aim = 0

    with open(filename) as f:
        for line in f:
            direction, num = line.split(" ")
            if direction == "forward":
                distance += int(num)
                depth = depth + (aim * int(num))
            elif direction == "up":
                aim -= int(num)
            elif direction == "down":
                aim += int(num)

    return depth * distance


if __name__ == "__main__":

    # Time tester
    start_time = time.time()
    out = p1("2021/day_2/input.txt")
    print(f"Part 1 Answer: {out}\nPart 1 Time: {time.time() - start_time} s")

    start_time = time.time()
    out = p2("2021/day_2/input.txt")
    print(f"Part 2 Answer: {out}\nPart 2 Time: {time.time() - start_time} s")
