import os
import time
import re
import pprint as pp
from itertools import dropwhile

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
    data = file.read()  # Read and strip whitespace

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

def split_data(data):
    '''Split data in to two parts, Crates and Instructions '''
    parts = data.split('\n\n')
    crates = (parts[0])
    instructions_str = (parts[1])
    insturctions = instructions_str.split('\n') 
    return crates, insturctions

def split_instructions(instruction:str):
    '''use re to split instructions in to three parts'''

    pattern = (r'move (\d+) from (\d+) to (\d+)')
    
    match = re.match(pattern, instruction)
    if match:
        number_of_boxes = match.group(1)
        number_of_boxes = int(number_of_boxes)
        start           = match.group(2)
        start           = int(start)
        end             = match.group(3)
        end             = int(end)

    return number_of_boxes, start, end

    #print(f' I\'m moving {number_of_boxes} boxes from , pile {start}, to pile {end}')

def split_stacks(stacks:list):
    '''split stacks in to lists'''
    stacks_list = [list() for _ in range(9)]
    length = len(stacks[-1])

    for level in stacks:
        stack_id = 0
        for char in range(1, length, 4):
            stacks_list[stack_id].append(level[char])
            stack_id += 1

    stripped_data = [list(dropwhile(lambda x: x == ' ', row)) for row in stacks_list]
    #for i in range(9):
       # print(stripped_data[i])
    return stripped_data






def run_instruction_9000(number_of_boxes:int, start:int, end:int, stacks:list):
    
    #removal
    
    for i in range(0,number_of_boxes):
        box = stacks[start-1].pop(0)
        print(f'remove {box} from stack {start}')
        stacks[end-1].insert(0, box)
        print(f'add {box} added to {end}')
    print('')
    
    return stacks

def run_instruction_9001(number_of_boxes:int, start:int, end:int, stacks:list):
    
    #removal
    
    for i in range(0,number_of_boxes):
        box = stacks[start-1].pop(0)
        print(f'remove {box} from stack {start}')
        stacks[end-1].insert(0+i, box)
        print(f'add {box} added to {end}')
    print('')
    
    return stacks
    
    

     

def part1(data):
    """Solve problem one."""
    
    storage, insturctions = split_data(data) #split the storage and instructions 
    stacks = storage.splitlines() #split storage in to stacks 

    stripped_data = split_stacks(stacks) #move stacks in to lists

    for instruction in insturctions:
        number_of_boxes, start, end = split_instructions(instruction)
        print(number_of_boxes, start, end)
        updated_stripped_data = run_instruction_9000(number_of_boxes, start, end, stripped_data)
        stripped_data = updated_stripped_data

    result = ''.join(stripped_data[i][0] for i in range(len(stripped_data)))
    print(result)
    
    
   
    



    
def part2(data):
    storage, insturctions = split_data(data) #split the storage and instructions 
    stacks = storage.splitlines() #split storage in to stacks 

    stripped_data = split_stacks(stacks) #move stacks in to lists

    for instruction in insturctions:
        number_of_boxes, start, end = split_instructions(instruction)
        print(number_of_boxes, start, end)
        updated_stripped_data = run_instruction_9001(number_of_boxes, start, end, stripped_data)
        stripped_data = updated_stripped_data

    result = ''.join(stripped_data[i][0] for i in range(len(stripped_data)))
    print(result)

if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)
