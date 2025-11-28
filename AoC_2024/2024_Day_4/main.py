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


directions = (
    (-1, 0),  # UP
    (-1, 1),  # UP RIGHT
    (0, 1),   # RIGHT
    (1, 1),   # DOWN RIGHT
    (1, 0),   # DOWN
    (1, -1),  # DOWN LEFT
    (0, -1),  # LEFT
    (-1, -1)  # UP LEFT
)

def can_move(word_search, x, y, direction):
    can_move_x  = x + direction[1]*3
    can_move_y  = y + direction[0]*3

    if can_move_y < 0 or can_move_y >= len(word_search):
        return False
    if can_move_x < 0 or can_move_x >= len(word_search[0]):
        return False

    return True

def is_xmas(word_search, x,y, direction):
    if word_search[y + direction[0]*1][x + direction[1]*1] != "M":
        return False
    if word_search[y + direction[0]*2][x + direction[1]*2] != "A":
        return False
    if word_search[y + direction[0]*3][x + direction[1]*3] != "S":
        return False
    return True

def part1(data):
    """Solve problem one."""
    word_search = data.splitlines()
    count = 0
    for row in range(len(word_search)):
        for col in range(len(word_search[0])):
            if word_search[col][row] == "X":
                for direction in directions:
                    if can_move(word_search,row,col,direction) and is_xmas(word_search, row,col, direction):
                        count +=1
    print(count)

    
        

def part2(data):
    """Solve problem two."""
    pass  # Add the logic for part 2 here

if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)
