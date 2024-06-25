
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
def p2(filename): #TODO: Fix the atrocious code
    """
    """

    total = 0

    with open(filename) as f:
        lines = f.readlines()

        width = len(lines[0])

        lines = ['.'*(width+1)] + ['.' + line.strip("\n") + '.' for line in lines] + ['.'*(width+1)]

        # print(lines)

        for i, line in enumerate(lines):
            matches = re.finditer(r'\*', line)



            

            for match in matches:

                last_line = lines[i-1]
                current_line = lines[i]
                next_line = lines[i+1]

                loc_star = match.start()
                # number = match.group()

                # print(loc, number)

                top = lines[i-1][loc_star-1:loc_star+2]
                left = lines[i][loc_star-1:loc_star]
                right = lines[i][loc_star+1:loc_star+2]
                bottom = lines[i+1][loc_star-1:loc_star+2]
                # print(check_box)

                result = re.findall(r'\d+', top) + re.findall(r'\d+', left) + re.findall(r'\d+', right) + re.findall(r'\d+', bottom)

                # print(result)

                check_box = top + left + '*' + right + bottom

                gear_ratio = 1

                if len(result) == 2:
                    
                    matches = re.finditer(r'\d+', top)

                    for match in matches:

                        loc_num = match.start()

                        matches_2 = re.finditer(r'\d+', last_line)

                        for match_2 in matches_2:
                            span = match_2.span()

                            if span[0] <= loc_star - 1 + (loc_num%3) < span[1]:
                                gear_ratio *= int(match_2.group())


                    matches = re.finditer(r'\d+', left)

                    for match in matches:

                        loc_num = loc_star+1

                        matches_2 = re.finditer(r'\d+', current_line)

                        for match_2 in matches_2:
                            span = match_2.span()

                            if span[0] <= loc_star - 1 < span[1]:
                                gear_ratio *= int(match_2.group())


                    matches = re.finditer(r'\d+', right)

                    for match in matches:

                        loc_num = loc_star+1

                        matches_2 = re.finditer(r'\d+', current_line)

                        for match_2 in matches_2:
                            span = match_2.span()

                            if span[0] <= loc_star + 1 < span[1]:
                                gear_ratio *= int(match_2.group())

                    matches = re.finditer(r'\d+', bottom)

                    for match in matches:

                        loc_num = match.start()

                        matches_2 = re.finditer(r'\d+', next_line)

                        for match_2 in matches_2:
                            span = match_2.span()

                            if span[0] <= loc_star - 1 + (loc_num%3) < span[1]:
                                gear_ratio *= int(match_2.group())

                    # print("gear_ratio: ", gear_ratio)
                    total += gear_ratio

    return total


if __name__ == "__main__":

    # Time tester
    start_time = time.time()
    out = p1("2023/day_3/input.txt")
    print(f"Part 1 Answer: {out}\nPart 1 Time: {(time.time() - start_time)*1000:.3f} ms")

    start_time = time.time()
    out = p2("2023/day_3/input.txt")
    print(f"Part 2 Answer: {out}\nPart 2 Time: {(time.time() - start_time)*1000:.3f} ms")
