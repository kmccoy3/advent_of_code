#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Advent of Code 2023 Day 5.
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
import numpy as np
import re



# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def read_data(filename):
    with open(filename) as f:
        data = f.read()

        data = data.split(':')
        
        return [re.findall(r'\d+', line) for line in data]
    
def convert_data(data):
    data = [np.array(data, dtype=int) for data in data]
    
    return data[1:]
            
def extract_data(data):

    seeds = data[0]
    maps = [np.reshape(data[i], (-1, 3)) for i in range(1, len(data))]

    return seeds, maps

def num_converter(seed, maps, layer):
    rows, cols = maps[layer].shape
    for i in range(rows):
        if int(seed) in range(maps[layer][i][1], maps[layer][i][1] + maps[layer][i][2]):
            return int(seed) - maps[layer][i][1] + maps[layer][i][0]
        
    return seed
        


def seed_to_loc(seed, maps):
    for layer in range(len(maps)):
        seed = num_converter(seed, maps, layer)

    return seed

    

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

    seeds, maps = extract_data(convert_data(read_data(filename)))

    locs = list()
    for seed in seeds:
        locs.append(seed_to_loc(seed, maps))

    return min(locs)


# Part 2 function
def p2(filename): 
    """
    """

    pass


# =============================================================================
# SCRIPT EXECUTION
# =============================================================================


if __name__ == "__main__":

    # Time tester
    start_time = time.time()
    out = p1("2023/day_5/input.txt")
    print(f"Part 1 Answer: {out}\nPart 1 Time: {(time.time() - start_time)*1000:.3f} ms")

    start_time = time.time()
    out = p2("2023/day_5/input.txt")
    print(f"Part 2 Answer: {out}\nPart 2 Time: {(time.time() - start_time)*1000:.3f} ms")
