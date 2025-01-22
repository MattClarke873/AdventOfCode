import os
import time
import re
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

def pattern(string):
    pattern = r'(\d+)-(\d+) (\S+): (\S+)'
    match = re.search(pattern,string)
    if match:
        lower_range = (match.group(1))
        upper_range = (match.group(2))
        key = (match.group(3))
        password = (match.group(4))

    return int(lower_range), int(upper_range), key, password

def check(lower_range:int, upper_range:int, key, password):
    count = password.count(key)
    if count >= lower_range and count <= upper_range:
        return True
    
def check_2(lower_range:int, upper_range:int, key, password):
    for char in range(len(password)-1):
        if (password[lower_range-1] == key or password[upper_range-1] == key) and not (password[lower_range-1] == key and password[upper_range-1] == key):
            return True


def part1(data):
    """Solve problem one."""
    count = 0
    passwords = sort_data(data)
    for password in passwords:
        lower_range, upper_range, key, string = pattern(password)
        if check(lower_range, upper_range, key, string):
            count += 1
    print(count)



def part2(data):
    """Solve problem two."""
    count = 0
    passwords = sort_data(data)
    for password in passwords:
        lower_range, upper_range, key, string = pattern(password)
        if check_2(lower_range, upper_range, key, string):
            count += 1
    print(count)

if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)
