''' This is Day *** '''
import time 
from itertools import permutations

import os
import time

# Terminal color codes
RED = '\033[31m'     # Red
RED_BG = '\033[41m'  # Red background
GREEN_BG = '\033[42m'
INVERSE = '\033[7m'  # Inverse mode
RESET = '\033[0m'    # Reset to default



# Get the absolute path of the current script
script_path = os.path.abspath(__file__)
# Get the folder where the script is saved
script_folder = os.path.dirname(script_path)
# Extract just the last folder name

file_path = os.path.join(script_folder, 'test_data.txt')

# Check if the file exists
if not os.path.isfile(file_path):
    # Create the file if it doesn't exist
    with open(file_path, 'w') as file:
        file.write('')



last_folder = os.path.basename(script_folder)
# Extract year and day
YEAR = int(last_folder.split('_')[0])  # Extract the part before the first '_'
DAY = int(last_folder.split('_')[-1])  # Extract the part after the last '_'
# File paths
data_file = f'/Users/MattClarke/repo/Advent of Code/AoC/AdventOfCode/AdventOfCode/AoC_{YEAR}/{YEAR}_Day_{DAY}/data.txt'
test_data_file = f'/Users/MattClarke/repo/Advent of Code/AoC/AdventOfCode/AdventOfCode/AoC_{YEAR}/{YEAR}_Day_{DAY}/test_data.txt'

# Read the main data file
with open(data_file, 'r', encoding="utf-8") as file:
    data = file.read().strip()  # Read and strip whitespace

# Read the test data file
with open(test_data_file, 'r', encoding="utf-8") as file:
    test_data = file.read().strip()  # Read and strip whitespace

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



dist = {}
towns = []


def part1(data):
    """Function Solves problem one."""
    lines = data.splitlines()
    for i in lines:
        l, r = i.strip().split(' = ')
        d =int(r)
        t1 ,t2 = l.split(' to ')
        dist[(t1, t2)]= d
        dist[(t2, t1)]= d
        if t1 not in towns:
            towns.append(t1)
        if t2 not in towns:
            towns.append(t2)
        
    for key, value in dist.items():
        print(key, value)
    print(towns)
    

    shortest = 9999999
    for r in permutations(towns):
        z = 0
        for i in range(len(r)-1):
            z += dist[(r[i],r[i+1])]

    shortest = min(shortest, z)
    print(shortest)

def part2(data):
    """Function Solves problem two."""

    print("not 719, too high")




if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)