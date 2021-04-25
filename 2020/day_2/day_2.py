
"""Advent of Code 2020 Day 2."""

# Import necessary libraries
import time


# Part 1 Function
def p1(filename):
    """
    Return the number of valid passwords.

    Parameters
    ----------
    filename : str
        The input filename of passwords.

    Returns
    -------
    count : int
        Number of valid passwords

    """
    # Read in data
    with open(filename) as f:
        lines = f.readlines()

    # Initialize valid password count
    count = 0

    # Loop through each password
    for line in lines:
        # Split line
        line = line.split(' ')
        nums = line[0].split('-')
        num1, num2 = int(nums[0]), int(nums[1])
        letter = line[1][0]
        password = line[2]

        # Count occurences of letter
        i = password.count(letter)

        # Update count
        if i >= num1 and i <= num2:
            count += 1

    return count


# Part 2 Function
def p2(filename):
    """
    Return the number of valid passwords.

    Parameters
    ----------
    filename : str
        The input filename of passwords.

    Returns
    -------
    count : int
        Number of valid passwords

    """
    # Read in data
    with open(filename) as f:
        lines = f.readlines()

    # Initialize valid password count
    count = 0

    # Loop through each password
    for line in lines:
        # Split line
        line = line.split(' ')
        nums = line[0].split('-')
        num1, num2 = int(nums[0]), int(nums[1])
        letter = line[1][0]
        password = line[2]

        # Test placements of letter
        log1 = password[num1-1] == letter
        log2 = password[num2-1] == letter

        # Update count
        if log1 + log2 == 1:
            count += 1

    return count


# Time tester
start_time = time.time()
out = p1("passwords.txt")
print("Part 1 took", time.time() - start_time, "seconds to run.")

start_time = time.time()
out = p2("passwords.txt")
print("Part 2 took", time.time() - start_time, "seconds to run.")
