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


def list_item(zone:str):
    '''
    for each line passed in to the function split using the "-" delimitor and to create
    start and stop point, the create a list from start - stop and return'''

    zone_range = []
    start,finish = zone.split('-')   # split items using the "-" as a delimitor

    for i in range(int(start),int(finish)+1):
        zone_range.append(i)
    return zone_range

def part1(data):
    """Solve problem one."""
    pairs = data.splitlines()  #Split data in to lines
    matched_area = 0 # create a marker and set to 0
    
    for pair in pairs: 
        elf1, elf2 = pair.split(',')  # Split each line in to 2 items.
        
        
        Elf1_zone = (list_item((elf1)))
        Elf2_zone = (list_item((elf2)))

        if all(item in Elf2_zone for item in Elf1_zone) or all(item in Elf1_zone for item in Elf2_zone): #if ALL of zone 1 in zone 2 or zone 2 in zone 1 add one
            matched_area += 1
    print(f'Areas with complete overlap = {matched_area}') 
        


def part2(data):
    """Solve problem two."""
    pairs = data.splitlines()
    matched_area = 0
    
    for pair in pairs:
        elf1, elf2 = pair.split(',')
        
        Elf1_zone = (list_item((elf1)))
        Elf2_zone = (list_item((elf2)))

        if any(item in Elf2_zone for item in Elf1_zone) or any(item in Elf1_zone for item in Elf2_zone): #if ANY of zone 1 in zone 2 or zone 2 in zone 1 add one
            matched_area += 1
    print(f'areas with ANY overlap = {matched_area}')

if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)
