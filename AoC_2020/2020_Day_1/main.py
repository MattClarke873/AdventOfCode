import time

# Terminal color codes
RED = '\033[31m'
RESET = '\033[0m'

# Constants for the year and day (customize these as needed)
YEAR = 2020
DAY = 1

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
    

def part1(data):
    """Solve problem one."""
    numbers = sort_data(data)
    for num_1 in range(len(numbers)):
        for num_2 in range(len(numbers)):
            for num_3 in range(len(numbers)):    
                if int(numbers[num_1]) + int(numbers[num_2]) + int(numbers[num_3]) == 2020:
                    print(f'The numbers are {numbers[num_1]} and {numbers[num_2]} and {numbers[num_3]}')
                    print(int(numbers[num_1]) * int(numbers[num_2]) * int(numbers[num_3]))
                    return

def part2(data):
    """Solve problem two."""
    pass  # Add the logic for part 2 here

if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)
