
"""Advent of Code 2023 Day 2."""

# Import necessary libraries
import time
import re


def parse_color_string(color_string):
    # Remove any leading or trailing spaces
    color_string = color_string.strip()
    
    # Split the string by commas to separate different color entries
    color_entries = color_string.split(',')
    
    # Initialize an empty dictionary to store the result
    color_dict = {}
    
    # Iterate over each entry
    for entry in color_entries:
        # Strip any leading or trailing spaces from the entry
        entry = entry.strip()
        
        # Split the entry into quantity and color
        quantity, color = entry.split(' ', 1)
        
        # Convert quantity to an integer and strip any leading/trailing spaces from the color
        color_dict[color.strip()] = int(quantity)
    
    return color_dict



# Part 1 function
def p1(filename):
    """
    Return the sum of all possible game IDs.

    Parameters
    ----------
    filename : str
        The input filename of the data.

    Returns
    -------
    total : int
        The total of all possible game IDs.
    """



    real_cubes = {"red": 12, "green": 13, "blue": 14}

    with open(filename) as f:

        total = 0

        for line in f.readlines():

            cond = True

            # print(line)

            vec = line.split(" ")

            game_id = int(re.findall(r"\d+", vec[1])[0])

            # print(game_id)

            hands = " ".join(vec[2:]).split(";")

            for hand in hands:

                out_dict = parse_color_string(hand)

                for color, count in out_dict.items():

                    if count > real_cubes[color]:
                        cond = False
                        break

            if cond:
                total += game_id

    return total



# Part 2 function
def p2(filename):
    """
    Return the total power of all games.

    Parameters
    ----------
    filename : str
        The input filename of the data.

    Returns
    -------
    total : int
        The total of all powers. Powers is the product of the minimum number 
        of cubes in the game.
    """

    with open(filename) as f:

        total = 0

        for line in f.readlines():

            red_min, blue_min, green_min = 1,1,1


            vec = line.split(" ")

            hands = " ".join(vec[2:]).split(";")



            for hand in hands:

                out_dict = parse_color_string(hand)

                if "red" in out_dict:
                    red_min = max(out_dict["red"], red_min)
                if "green" in out_dict:
                    green_min = max(out_dict["green"], green_min)
                if "blue" in out_dict:
                    blue_min = max(out_dict["blue"], blue_min)


            power = red_min * green_min * blue_min

            total += power

    return total


if __name__ == "__main__":

    # Time tester
    start_time = time.time()
    out = p1("2023/day_2/input.txt")
    print(f"Part 1 Answer: {out}\nPart 1 Time: {(time.time() - start_time)*1000:.3f} ms")

    start_time = time.time()
    out = p2("2023/day_2/input.txt")
    print(f"Part 2 Answer: {out}\nPart 2 Time: {(time.time() - start_time)*1000:.3f} ms")
