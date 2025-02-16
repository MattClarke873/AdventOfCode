import os
import time
import re
import pprint
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


def sort_data(data):
    return data.splitlines()

def part1(data):
    """Solve problem one."""
    ls = False
    lines = (sort_data(data))

    file_direct = [[], [], []]
    
    level = 0  # Initialize the level
    

    for line in range(len(lines)):
        if lines[line] == "$ cd /":
            level = 0
        elif lines[line] == "$ ls":
            ls = True
        elif lines[line] == "$ cd ..":
            level -= 1
        elif lines[line].startswith('$ cd') and lines[line] != "$ cd /" and lines[line] != "$ cd ..":
            level +=1 #print(line.split(' ')[2]) #move to this file
            pass
        elif lines[line].startswith("$"):
            ls = False


        
        if ls:
            if lines[line].startswith('dir'):
                direct_name = lines[line].split(' ')[1]  # Get the directory name after 'dir'
                
                # Ensure the dictionary exists in the specific level
                if not any(direct_name in d for d in file_direct[level]):
                    file_direct[level].append({direct_name: []})



            elif re.match(r'^\d+', lines[line]):
                file_size = int(lines[line].split(' ')[0])  # Get the file size as an integer
                file_name = lines[line].split(' ')[1]  # Get the file name
                # Add a value to the 'goal' list
                value_to_add = "new_value"
                for item in file_direct[level]:
                    if direct_name in item:
                        item[direct_name].append(file_name)

    
                
                











    for line in file_direct:
        print(line)
 
        
    
            
            




def part2(data):
    """Solve problem two."""
    pass  # Add the logic for part 2 here

if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, test_data)
    answer2 = time_it(part2, data)
