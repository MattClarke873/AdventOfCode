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

def sort_data(data):
    return data.splitlines()

def moving(data_set:list, row_step:int, coloum_step:int):
    row, coloum, count = 0, 0, 0
    
    while row < len(data_set):
        row_list = list(data_set[row])
        if (row_list[coloum]) == "#":
            count += 1
        row += row_step 
        coloum = (coloum + coloum_step) % len(data_set[0])
    return count

        
    


def part1(data):
    """Solve problem one."""
    lines = sort_data(data)
    
    print(moving(lines,1,3))
    
    

    
    


def part2(data):
    """Solve problem two."""
    pass  # Add the logic for part 2 here
    lines = sort_data(data)
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    
    # Calculate the product of tree counts for all slopes
    result = 1
    for row_step, col_step in slopes:
        result *= moving(lines, row_step, col_step)
    
    print(result)
    
    

if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)
