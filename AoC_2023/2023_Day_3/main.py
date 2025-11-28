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

def parse_data(data):
    """Take the data and turn it in to a gird, then return the grid and number of rows/cols"""
    lines = data.splitlines()
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0])
    return grid, rows, cols



def get_targets(grid):
    """Take grid input and find the symbols that are needed for targeting the part numbers""" 
    
    targets = set()

    for row in grid:
        for char in row:
            if not char.isdigit() and char != ".":
                targets.add(char)

    return targets



def find_neighbors(grid, targets):
    """Find the neighbours of the targets"""
    digit_hit = set()
   
    directions = [
        (-1,  0),  # up
        (-1,  1),  # up-right
        ( 0,  1),  # right
        ( 1,  1),  # down-right
        ( 1,  0),  # down
        ( 1, -1),  # down-left
        ( 0, -1),  # left
        (-1, -1)   # up-left
    ]

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char in targets:
                for dy, dx in directions:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]):
                        neighbor_char = grid[ny][nx]
                        if neighbor_char.isdigit():
                            digit_hit.add((ny,nx))

  
    return sorted(digit_hit)


def find_gears(grid):
    """Find the neighbours of the targets"""
    count = 0
    digit_hit = set()
   
    directions = [
        (-1,  0),  # up
        (-1,  1),  # up-right
        ( 0,  1),  # right
        ( 1,  1),  # down-right
        ( 1,  0),  # down
        ( 1, -1),  # down-left
        ( 0, -1),  # left
        (-1, -1)   # up-left
    ]

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "*":
                for dy, dx in directions:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]):
                        neighbor_char = grid[ny][nx]
                        if neighbor_char.isdigit() and count <2:
                            digit_hit.add((ny,nx))
                            count+=1
                        if neighbor_char.isdigit() and count == 2:
                            digit_hit.add((ny,nx))
                            count = 0
                            pass
                        
    
    return sorted(digit_hit)






def find_part_number(grid, digit_hit):
    start_points = set()
    for row, col in digit_hit:
        # move left until the start of the number
        start = col
        while start > 0 and grid[row][start - 1].isdigit():
            start -= 1
        start_points.add((row,start))
    return (sorted(start_points))


def complete_number(grid, start_points):
    numbers = []
    for row, col in start_points:
        number = []
        working = col
        while working < len(grid[row]) and grid[row][working].isdigit():
            number.append(grid[row][working])
            working+=1
        
        numbers.append(int("".join(number)))  # convert to int
    print(sum(numbers))
    


def complete_gear(grid, start_points):
    numbers = []
    for row, col in start_points:
        number = []
        working = col
        while working < len(grid[row]) and grid[row][working].isdigit():
            number.append(grid[row][working])
            working+=1
        numbers.append(int("".join(number)))  # convert to int

    return list(numbers)



def work_gears(list):
    numbers = []

    for index, coord in enumerate(list):
        if (index % 2) == 0:
            a = coord
        elif (index % 2) != 0:
            b = coord   
            numbers.append(a* b)
    return sum(numbers)
                            



def part1(data):
    """Solve problem one."""
    
    grid, row, col = parse_data(data)
    targets= get_targets(grid)
    digit_hit = (find_neighbors(grid, targets))
    start_points = find_part_number(grid, digit_hit)
    complete_number(grid, start_points)
            

def part2(data):
    """Solve problem two."""
    grid, row, col = parse_data(data)
    gears_match = find_gears(grid)
    start_points = find_part_number(grid, gears_match)
    complete_gear_list = complete_gear(grid, start_points)
    print(work_gears(complete_gear_list))
    
      

if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, test_data)
