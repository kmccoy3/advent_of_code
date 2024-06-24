
"""Advent of Code 2023 Day 3."""

# Import necessary libraries
import time
import re


# Part 1 function
def p1(filename):
    """
    Return the sum of all part numbers.

    Parameters
    ----------
    filename : str
        The input filename of the data.

    Returns
    -------
    total : int
        The total of all part numbers.
    """

    # TODO: Add comments
    total = 0

    with open(filename) as f:
        lines = f.readlines()

        width = len(lines[0])

        lines = ['.'*(width+1)] + ['.' + line.strip("\n") + '.' for line in lines] + ['.'*(width+1)]

        for i, line in enumerate(lines):
            matches = re.finditer(r'\d+', line)

            for match in matches:

                begin = match.start()
                end = match.end()
                number = match.group()

                check_box = lines[i-1][begin-1:end+1] + lines[i][begin-1:end+1] + lines[i+1][begin-1:end+1]

                result = re.findall(r'[^.|(0-9)]', check_box)

                if len(result) != 0:
                    total += int(number)

    return total



# Part 2 function
def p2(filename):
    """
    """

    with open(filename) as f:

        pass


if __name__ == "__main__":

    # Time tester
    start_time = time.time()
    out = p1("2023/day_3/input.txt")
    print(f"Part 1 Answer: {out}\nPart 1 Time: {(time.time() - start_time)*1000:.3f} ms")

    # start_time = time.time()
    # out = p2("2023/day_3/input.txt")
    # print(f"Part 2 Answer: {out}\nPart 2 Time: {(time.time() - start_time)*1000:.3f} ms")
