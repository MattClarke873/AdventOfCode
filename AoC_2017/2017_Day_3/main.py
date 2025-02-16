''' This is Day *** '''
import time 
import os
from collections import defaultdict


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

def get_spiral():
    pass

def part1(data):
    """Function Solves problem one."""
    layer = 0
    while (2 * layer + 1)**2 < int(data):
        layer += 1
    print(f'the layer is: {layer}')

    max_val_lay = (2*layer +1)**2
    print(f'The square val of this layer is: {max_val_lay} (bottom right corner)')


    steps_back= max_val_lay - int(data)
    print(f'steps from data to sqr of layer {steps_back}')
    side_length = 2 * layer + 1
    print(f'side length is {side_length}')

    side_position = steps_back % side_length  # Position along the current side
    x, y = 0, 0
    if steps_back < side_length:  # Bottom side
        x = layer
        y = -layer + side_position
    elif steps_back < 2 * side_length:  # Left side
        x = layer - (side_position + 1)
        y = -layer
    elif steps_back < 3 * side_length:  # Top side
        x = -layer
        y = -layer + (side_position + 1)
    else:  # Right side
        x = -layer + (side_position + 1)
        y = layer

    print(x, y)
    print(f'result for part 1 is {abs(x) + abs(y)}')

def part2(data):
    """Function Solves problem two."""

    grid = defaultdict(int)
    grid[(0,0)] = 1






if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)



