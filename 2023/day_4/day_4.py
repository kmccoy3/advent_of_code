#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Advent of Code 2023 Day 4.
"""


# =============================================================================
# AUTHOR INFORMATION
# =============================================================================


__author__ = "Kevin McCoy"
__copyright__ = "Copyright 2024, McCoy"
__credits__ = ["Kevin McCoy"]
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Kevin McCoy"
__email__ = ["kevin@kmccoy.net"]
__status__ = "development"
__date__ = "2024-06-25" # Last modified date


# =============================================================================
# IMPORTS
# =============================================================================


import time
import re


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================


def get_num_matches(line):
    winning_nums = line[8:].split('|')[0]
    my_nums = line[8:].split('|')[1]

    # Extract the numbers from the strings
    winning_nums = [int(num) for num in re.findall(r'\d+', winning_nums)]
    my_nums = [int(num) for num in re.findall(r'\d+', my_nums)]

    matches = set(winning_nums).intersection(set(my_nums))

    return len(matches)


# =============================================================================
# MAIN FUNCTIONS
# =============================================================================


# Part 1 function
def p1(filename):
    """
    Return the sum of all points.

    Parameters
    ----------
    filename : str
        The input filename of the data.

    Returns
    -------
    total : int
        The total of all points won by your cards.
    """

    #TODO: Add more comments

    # Initialize running total of points
    total = 0

    # Read the input file, loop through lines
    with open(filename) as f:
        for i, line in enumerate(f.readlines()):

            # Card number is the line number
            matches = get_num_matches(line)

            points = 0 if matches == 0 else 2**(matches-1)

            total += points

    return total



# Part 2 function
def p2(filename): 
    """
    """

    # Total SCORECARDS
    total = 0
    N = 198
    scorecards = {i: 1 for i in range(1, N+1)}

    # Read the input file, loop through lines
    with open(filename) as f:
        for i, line in enumerate(f.readlines()):


            matches = get_num_matches(line)

            for j in range(i+2, i+matches+2):
                scorecards[j] += scorecards[i+1]

    return sum(scorecards.values())


# =============================================================================
# SCRIPT EXECUTION
# =============================================================================


if __name__ == "__main__":

    # Time tester
    start_time = time.time()
    out = p1("2023/day_4/input.txt")
    print(f"Part 1 Answer: {out}\nPart 1 Time: {(time.time() - start_time)*1000:.3f} ms")

    start_time = time.time()
    out = p2("2023/day_4/input.txt")
    print(f"Part 2 Answer: {out}\nPart 2 Time: {(time.time() - start_time)*1000:.3f} ms")
