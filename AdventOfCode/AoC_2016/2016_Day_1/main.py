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


def sortData(str:str):
    
    direction = str.strip()[0]
    units = str.strip()[1:]
    units = int(units)
    return direction, units


def turning(current_direction, direction):

    if current_direction == "N":
        if direction == "L":
            return "W"
        if direction == "R": 
            return "E"
    elif current_direction == "E":
        if direction == "L":
            return "N"
        if direction == "R":
            return "S"
    elif current_direction == "S":
        if direction == "L":
            return "E"
        if direction == "R":
            return "W"
    elif current_direction == "W":
        if direction == "L":
            return "S"
        if direction == "R":
            return "N"
        

def moving(pole, current_x:int, current_y:int, moving:int):

    if pole == "N":
        current_y += moving
        current_x = current_x
    if pole == "S":
        current_y -= moving
        current_x = current_x
    if pole == "E":
        current_x += moving
        current_y = current_y
    if pole == "W":
        current_x -= moving
        current_y = current_y

    return current_x , current_y

def fullPath(pole, current_x:int, current_y:int, moving:int, visited:set):
    
    for _ in range(moving):  
        if pole == "N":
            current_y += 1
            current_x =  current_x
        if pole == "S":
            current_y -= 1
            current_x =  current_x
        if pole == "E":
            current_x += 1
            current_y =  current_y
        if pole == "W":
            current_x -= 1
            current_y =  current_y
        

        if (current_x,current_y) in visited: 
            print (f'the answer is {RED_BG}{abs(current_x) + abs(current_y)}{RESET}')
            
        else:
            visited.add((current_x,current_y))
    
    return current_x , current_y, visited
         
def find_first_repeated(lst):
    seen = set()
    for num in lst:
        if num in seen:
            return num
            break  # Return the first number that repeats
        seen.add(num)
    return None  # Return None if no repetition is found




def part1(data):
    """Solve problem one."""
    pole = "N"
    y = 0
    x = 0
    instructions = data.strip().split(',')

    for i in instructions:
        direction, units = (sortData(i))
        pole = turning(pole, direction)
        x, y = moving(pole, x, y, units)
    print(f'move {units} steps {pole} |||| {x} across and {y} vertically |||| manhatan is {abs(x)+abs(y)}')


def part2(data):
    """Solve problem two."""
    pole = "N"
    x, y = 0, 0
    
    visited = set() 
    instructions = data.strip().split(',')

    for i in instructions:
        direction, units = (sortData(i))
        pole = turning(pole, direction)
        x, y, visited = fullPath(pole, x, y, units, visited)
        
        


    
    


if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)
