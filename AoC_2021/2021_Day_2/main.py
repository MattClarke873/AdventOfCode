import os
import time

# Terminal color codes
RED = '\033[31m'
RESET = '\033[0m'



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

def part1(data):
    """Solve problem one."""
    instructions = data.splitlines()
    depth = 0
    distance = 0

    for i in instructions:
        if i.startswith('forward'):
            distance += int(i[-1:])
        if i.startswith('up'):
            depth -= int(i[-1:])
        if i.startswith('down'):
            depth += int(i[-1:])

    print(f'distance = {distance}, depth = {depth}, dig = {distance*depth}')


def part2(data):
    """Solve problem two."""
    instructions = data.splitlines()
    depth = 0
    distance = 0
    aim = 0

    for i in instructions:
        if i.startswith('down'):
            aim += int(i[-1:])
        if i.startswith('up'):
            aim -= int(i[-1:])
        if i.startswith('forward'):
            distance += int(i[-1:])
            depth += aim*int(i[-1:])
        print(f'{i:<10}   - Horiz {distance:<5} Aim {aim} * {i[-1:]:<5} Depth {depth}')   

    print(f'distance = {(distance):<10} depth = {depth:<10} diag = {distance*depth}')

if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)
