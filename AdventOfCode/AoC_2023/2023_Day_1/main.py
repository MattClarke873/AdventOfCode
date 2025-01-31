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

def replacement(text:str):
    '''take in a mixed string (e.g '4nineeightseven2') and return full int (49872) '''
    word_to_digit = {"one": "1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8",  "nine":"9"}
    digits = []

    while text:
        if text[0].isdigit():
            digits.append(text[0])
            text = text[1:]
            continue
        for word in word_to_digit:
            if text.startswith(word):   
                digits.append(word_to_digit[word])
                text = text[1:]
                break
        else:
            text = text[1:]
    return digits
            

    




def forward(text:str):
    '''loop string and find first number
    the return as a STRING'''
    for char in (text):
        if char.isdigit():
            return char




def reverse(text:str):
    '''loop string IN REVERSE and find first number
    the return as a STRING'''
    for char in reversed(text):
        if char.isdigit():
            return char

def join_values(first:str, last:str):
    '''join to numbers a string, return value'''
    return first+last






def part1(data):
    """Solve problem one."""
    strings = data.splitlines()
    
    string_values = []

    for string in strings:
        string_values.append(int(join_values((forward(string)),(reverse(string)))))
    
    print(f'{RED_BG}{sum(string_values)}{RESET}')
        


def part2(data):
    """Solve problem two."""
    strings = data.splitlines()
    string_values = []

    for string in strings:
        new_string = ((replacement(string)))
        string_values.append(int(join_values((forward(new_string)),(reverse(new_string)))))

    print(f'{RED_BG}{sum(string_values)}{RESET}')
    
    
if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)
