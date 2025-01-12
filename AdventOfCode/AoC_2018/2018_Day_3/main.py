''' This is Day *** '''
import time 
import numpy as np
import matplotlib.pyplot as plt
import re


YEAR = 2018
DAY = 3
with open(f'/Users/MattClarke/repo/Advent of Code/AoC/AdventOfCode/AdventOfCode/AoC_{YEAR}/{YEAR}_Day_{DAY}/data.txt', 'r', encoding="utf-8") as file:
    data = file.read().strip()  # read file, and strip -- remove any white space

with open(f'/Users/MattClarke/repo/Advent of Code/AoC/AdventOfCode/AdventOfCode/AoC_{YEAR}/{YEAR}_Day_{DAY}/test_data.txt', 'r', encoding="utf-8") as file:
    test_data = file.read().strip()  # read file, and strip -- remove any white space    





def time_it(func, *args, **kwargs):
    """
    Measure the execution time of a function.
    
    Args:
        func: The function to time.
        *args: Positional arguments for the function.
        **kwargs: Keyword arguments for the function.
    
    Returns:
        result: The return value of the function.
        elapsed_time: The time taken to execute the function in seconds.
    """
    start_time = time.time()
    result = func(*args, **kwargs)
    elapsed_time = time.time() - start_time
    print(f"Execution time: {elapsed_time:.6f} seconds")
    return result



def part1(data):
    """Function Solves problem one."""

    # Create your 2D array (fabric)
    fabric = np.zeros((1000, 1000), dtype=int)
    IDS = []
    lines = data.splitlines()

    for line in lines:
        # Regular expression to extract values
        pattern = r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)"
        match = re.match(pattern, line)

        if match:
            id = f"#{match.group(1)}"
            Y_start = int(match.group(2))
            X_start = int(match.group(3))
            Y_range = int(match.group(4))
            X_range = int(match.group(5))

            # Update the fabric array for the current claim
            fabric[Y_start:(Y_start+Y_range), X_start:(X_start+X_range)] += 1
            IDS.append((id, Y_start, X_start, Y_range, X_range))
        else:
            print("No match found.")



    no_overlap_ids = []
    for claim in IDS:
        id, Y_start, X_start, Y_range, X_range = claim

        # Check if any values in the range are greater than 1 (i.e., overlap with another claim)
        if np.any(fabric[Y_start:(Y_start+Y_range), X_start:(X_start+X_range)] > 1):
            continue  # If overlap, skip this ID
        else:
            no_overlap_ids.append(id)  # No overlap, add to result

    # Output the list of IDs with no overlap
    print("Remaining IDs with no overlap:", no_overlap_ids)

    count_greater_than_1 = np.sum(fabric > 1)
    print(f"Number of values greater than 1: {count_greater_than_1}")
        
        

def part2(data):
    """Function Solves problem two."""
    




if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)