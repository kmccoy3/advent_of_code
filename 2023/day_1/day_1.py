
"""Advent of Code 2021 Day 1."""

# Import necessary libraries
import time
import re


# Part 1 function
def p1(filename):
    """
    Return the total of the first and last number of each line.

    Parameters
    ----------
    filename : str
        The input filename of the data.

    Returns
    -------
    total : int
        The total of all numbers encountered.
    """

    with open(filename) as f:

        # Initialize total
        total = 0

        # Loop over each line in file
        for line in f.readlines():
            # Extract and combine all numbers
            out = re.findall(r"\d+", line)
            out = ''.join(out)

            # Update total
            total += int(out[0] + out[-1])

    return total



# Part 2 function
def p2(filename):
    """
    Return the total of the first and last number of each line.

    Parameters
    ----------
    filename : str
        The input filename of the data.

    Returns
    -------
    total : int
        The total of all numbers encountered.
    """

    with open(filename) as f:

        # Initialize total
        total = 0

        # Define number words
        num_words = ["one", "two", "three", "four", "five",
                      "six", "seven", "eight", "nine"]

        # Create dictionary for number words
        num_dict = {num_words[i-1]: str(i) for i in range(1, 10)}

        # Create regex pattern
        reg_pattern = r"(?=([1-9]+|" + "|".join(num_words) +"))"

        # Loop over each line in file
        for line in f.readlines():
            # Extract and combine all numbers
            out = re.findall(reg_pattern, line)

            for i in range(len(out)): #FIXME: Avoid using a loop here
                if out[i] in num_dict:
                    out[i] = num_dict[out[i]]

            out = ''.join(out)

            # Update total
            total += int(out[0] + out[-1])

    return total


if __name__ == "__main__":

    # Time tester
    start_time = time.time()
    out = p1("2023/day_1/input.txt")
    print(f"Part 1 Answer: {out}\nPart 1 Time: {(time.time() - start_time)*1000:.3f} ms")

    start_time = time.time()
    out = p2("2023/day_1/input.txt")
    print(f"Part 2 Answer: {out}\nPart 2 Time: {(time.time() - start_time)*1000:.3f} ms")
