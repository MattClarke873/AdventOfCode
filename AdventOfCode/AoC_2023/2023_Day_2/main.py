import os
import time
import pprint
import re

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


def split(game:str):
    '''sort, strip, and split data, the add to lists'''
    
    game_id , hands = game.strip().split(":")
    turns = hands.strip().split(';')
    dice_numbers = {}

    for turn in turns:
        dice= turn.strip().split(',')
        for choice in dice:
            number, colour = choice.strip().split(' ')
            number = number.strip()
            number = int(number)
        

            if colour not in dice_numbers: 
                dice_numbers[colour] = number
            if dice_numbers[colour] <= number:
                dice_numbers[colour] = number 
    return game_id, dice_numbers




def check(game_id:str, dice_dict:dict):
    '''check if any of the dice are greater then the allowed limit'''
    
    number = game_id.strip().split(' ')[1]
    check_limit= {'red': 12, 'green': 13, 'blue': 14}
    
    print_flag= True
    for colour in check_limit:
        if colour in dice_dict:
            if dice_dict[colour] > check_limit[colour]:
                return 0
                break
            
    # Print the result only if all conditions are met
    if print_flag:
        return int(number)

      
def returnSum(myDict):
 
    res = 1
    for i in myDict:
        res = res * myDict[i]
    
    return res




def part1(data):
    """Solve problem one."""
    games = data.splitlines()

    sum_of_id = 0

    for game in games:
        game_id, colour_dict = split(game)
        #print(game_id, colour_dict)
        #print (check(game_id, colour_dict))
        sum_of_id += (check(game_id, colour_dict))
    print(f'Total = {RED_BG}{sum_of_id}{RESET}')



def part2(data):
    """Solve problem two."""
    games = data.splitlines()
    list = []
    for game in games:
        game_id, colour_dict = split(game)
        #print(game_id, colour_dict)
        list.append(returnSum(colour_dict))
    print(f'Sum of Multi colour list = {RED_BG}{sum(list)}{RESET}')
        
    



  

if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)


#3154 too high