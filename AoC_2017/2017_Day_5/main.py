import os
import time

# Terminal color codes
RED = '\033[31m'     # Red
RED_BG = '\033[41m'  # Red background
GREEN_BG = '\033[42m'
INVERSE = '\033[7m'  # Inverse mode
RESET = '\033[0m'    # Reset to default

import os

def get_file_paths():
    """
    Retrieves the script's directory, extracts the year and day from its name,
    ensures test_data.txt exists, and reads data from both files.

    Returns:
        tuple: (YEAR, DAY, data_file, test_data_file, data, test_data)
    """
    # Get script directory
    script_folder = os.path.dirname(os.path.abspath(__file__))
    last_folder = os.path.basename(script_folder)

    # Extract year and day dynamically from the folder name
    YEAR = int(last_folder.split('_')[0])
    DAY = int(last_folder.split('_')[-1])

    # File paths
    data_file = os.path.join(script_folder, 'data.txt')
    test_data_file = os.path.join(script_folder, 'test_data.txt')

    # Ensure test_data.txt exists
    if not os.path.isfile(test_data_file):
        with open(test_data_file, 'w') as file:
            file.write('')

    # Read data files
    with open(data_file, 'r', encoding="utf-8") as file:
        data = file.read().strip()
    
    with open(test_data_file, 'r', encoding="utf-8") as file:
        test_data = file.read().strip()

    return YEAR, DAY, data_file, test_data_file, data, test_data

# Usage
YEAR, DAY, data_file, test_data_file, data, test_data = get_file_paths()


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
    steps = [int(line) for line in data.splitlines()]
    i = 0
    count = 0
    while 0 <= i < len(steps):
        jump = steps[i]
        steps[i] += 1
        i += jump
        count += 1
    print(count)
'''steps = list'''
'''step = int'''
    

def part2(data):
    """Solve problem two."""
    steps = [int(line) for line in data.splitlines()]
    i = 0
    count = 0
    
    while 0 <= i < len(steps):
        jump = steps[i]
        if jump >= 3:
            steps[i] -= 1
            i += jump
            count += 1
        else:
            steps[i] += 1
            i += jump
            count += 1
    print(count)

if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)
