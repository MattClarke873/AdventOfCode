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

def sort_data(data, limiter):
    return re.split(limiter, data)
    return data.split(limiter)

def sep_draw_numbers(data):
    return data.split(',')


def part1(data):
    """Solve problem one."""
    """ call number
        check numbers
        do sum
        """

    numbers = sort_data(data, '\n\n')           #Split all data on empty line return
    call_numbers = (sort_data(numbers[0], ',')) #Separate all numbers in the call line 
    bingo_cards = [card.split() for card in numbers[1:]]  # Process the remaining cards into 2D arrays
    num_of_cards = (len(bingo_cards))
    

    for card in bingo_cards:
        for num in range(len(card)-1):
            print(type(card[num]))
            print(f'{card[num]:<5}{card[num+1]:<5}{card[num+2]:<5}{card[num+3]:<5}{card[num+4]:<5}')
            print(f'{card[num+5]:<5}{card[num+6]:<5}{card[num+7]:<5}{card[num+8]:<5}{card[num+9]:<5}')
            print(f'{card[num+10]:<5}{card[num+11]:<5}{card[num+12]:<5}{card[num+13]:<5}{card[num+14]:<5}')
            print(f'{card[num+15]:<5}{card[num+16]:<5}{card[num+17]:<5}{card[num+18]:<5}{card[num+19]:<5}')
            print(f'{card[num+20]:<5}{card[num+21]:<5}{card[num+22]:<5}{card[num+23]:<5}{card[num+24]:<5}')
            print('')








def part2(data):
    """Solve problem two."""
    pass  # Add the logic for part 2 here

if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)
