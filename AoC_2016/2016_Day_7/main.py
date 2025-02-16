import os
import time
import re

# Terminal color codes
RED = '\033[31m'     # Red
RED_BG = '\033[41m'  # Red background
GREEN_BG = '\033[42m'
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




def checkABBA(line):

    for section in line:
        if not section.startswith("["):
            for char in range(len(section)-3):
                if section[char] == section[char+3] and section[char+1] == section[char+2] and not section[char] == section[char+2]:
                    
                    return True



def checkeInnerABBA(line):

    for section in line:
        if section.startswith("["):
            
            for char in range(len(section)-3):
                if section[char] == section[char+3] and section[char+1] == section[char+2] and not section[char] == section[char+2]:
                    return True
                else:
                    False




def checkXYX(line:str):
    xyx = []
    count = 0

    for section in line:
        if not section.startswith("["):
            for char in range(len(section)-2):
                
                if section[char] == section[char+2] and section[char] != section[char+1]:
                    #print(string[char], string[char+1], string[char+2])
                    xyx.append([section[char], section[char+1]])
                    count +=1
                
    return xyx, count


def inBrackets(line:list, list:list):
    count = 0
     
    for pair in list:
        reverse = (pair[1]+pair[0]+pair[1])
        for section in line:
            if section.startswith("["):
                if reverse in section:
                    count +=1
                else:
                    pass
    return count
 


def part1(data):
    """Solve problem one."""
    lines = data.splitlines()
    count =0
    for line in lines:
        linesplit = re.split(r'(\[[^\]]*\])', line)
        first = checkABBA(linesplit)
        if first:
            count +=1
            second = checkeInnerABBA(linesplit)
            if second:
                count -=1
            
                
            
        
    print(count)




def part2(data):
    """Solve problem two."""
    lines = data.splitlines()
    count =0
    for line in lines:
        
        linesplit = re.split(r'(\[[^\]]*\])', line)
        
        xyx, first = (checkXYX(linesplit))
        second = inBrackets(linesplit, xyx)

        if first and second:
            count +=1
    print(count)




if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)
