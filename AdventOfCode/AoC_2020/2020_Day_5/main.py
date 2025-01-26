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



def sort_seats(instructions):
    rows = list(range(128))  # Rows from 0 to 127
    columns = list(range(8))  # Columns from 0 to 7
    sanity = []
    
    # Split the rows based on the first 7 characters
    for char in instructions[:7]:  # First 7 characters for row
        mid_row = len(rows) // 2
        if char == "F":
            rows = rows[:mid_row]  # Keep the front half
        elif char == "B":
            rows = rows[mid_row:]  # Keep the back half
    
    # Split the columns based on the last 3 characters
    for char in instructions[7:]:  # Last 3 characters for column
        mid_col = len(columns) // 2
        if char == "L":
            columns = columns[:mid_col]  # Keep the left half
        elif char == "R":
            columns = columns[mid_col:]  # Keep the right half
    
    # Return the final row and column
    print(f"Row: {rows[0]}, Column: {columns[0]}")
    
    return rows[0], columns[0]




def part1(data):
    """Solve problem one."""
    passengers = data.splitlines()
    sanity = []

    for passenger in passengers:
        row, column = sort_seats(passenger)
        sanity.append(row*8+column)

    print(sorted(sanity)[-1])
        



    
    



def part2(data):
    """Solve problem two."""
    pass  # Add the logic for part 2 here

if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)
