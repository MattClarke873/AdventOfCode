import os
import time

# Terminal color codes
RED = '\033[31m'     # Red
RED_BG = '\033[41m'  # Red background
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



def part1(data):
    """Function Solves problem one."""
    lines = data.strip().splitlines()  # Split input into individual lines and remove leading/trailing whitespace
    processed = []
    
    for line in lines:
        # Use split() to separate based on any whitespace and convert to integers
        numbers = list(map(int, line.split()))
        if len(numbers) == 3:  # Ensure there are exactly 3 integers per line
            processed.append(tuple(numbers))
        else:
            print(f"Invalid line skipped: {line}")  # Debugging for invalid lines
    
    #print(processed[0][0])

    count= 0
    for i in range(len(processed)):
        if ((processed[i][0] + processed[i][1] > processed[i][2]) and (processed[i][0] + processed[i][2] > processed[i][1]) and (processed[i][1] + processed[i][2] > processed[i][0])):
            count += 1
    print(f'possilbe = {RED_BG}{count}{RESET}')


def part2(data):
    """Function Solves problem two."""
    processed = []
    lines = data.strip().splitlines()  # Split input into individual lines and remove leading/trailing whitespace
    count= 0


    for line in lines:
        # Use split() to separate based on any whitespace and convert to integers
        numbers = list(map(int, line.split()))
        if len(numbers) == 3:  # Ensure there are exactly 3 integers per line
            processed.append(tuple(numbers))
        else:
            print(f"Invalid line skipped: {line}")  # Debugging for invalid lines
    
    for side in range(len(processed[0])):
        for i in range(0, len(processed)-2, 3):
            a =  (processed[i][side])
            b =  (processed[i+1][side])
            c =  (processed[i+2][side])
            
            
            if ((a + b > c) and (a + c > b) and (b + c > a)):
                count += 1
    print(f'possilbe = {RED_BG}{count}{RESET}')
        



if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)