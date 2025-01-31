import os
import time

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

def returnRemoveHypan(data):
    lines = data.splitlines()
    new_lines = []

    for line in lines:
        new_lines.append(line.replace("-", ""))
    return new_lines

def returnReplaceHypan(data):
    lines = data.splitlines()
    new_lines = []

    for line in lines:
        new_lines.append(line.replace("-", " "))
    return new_lines

def returnSplitData(line:str):
    a = line[-6:-1]
    b = line[:-7]
    

    return a, b

def returnSetCheckLetters(b:str):

    check_letters = []
            
    for char in b:
        if not char.isdigit():
            if char not in check_letters:
                check_letters.append(char)
                check_letters = sorted(check_letters)
    return check_letters


def returnSingles(name_value:list, name:str):
    singles = []
    for char in name_value:
        if name.count(char) < 2:
            singles.append(char)
            singles = sorted(singles)
    return singles


def returnMulti(name_value:list, name:str):
    multi = {}
    multi_list = []
    for char in name_value:
        if name.count(char) > 1 :
            multi[char]= name.count(char)
    sort_multi = dict(sorted(multi.items(), key=lambda item: item[1], reverse = True))
    return list(sort_multi.keys())

def returnMakeString(list:list):
    string= ""
    for i in list:
        string += i

    return string[:5]
            

def returnIDNum(line):
    string = ""
    doorname = line[:-7]
    for i in doorname:
        if i.isdigit():
            string += i
    return string



def shiftCipher(string:str, steps:int):

    min_val = 97
    max_val = 122
    new_string = ""

    for x in string:
    
        range_size = max_val - min_val + 1  # Calculate the size of the range
        new_value = ((ord(x) - min_val + steps) % range_size) + min_val
        if new_value != 32:
            new_string += chr(new_value)
        elif new_value == 32:
            new_string += " "
    return new_string






def part1(data):
    """Solve problem one."""
    lines = (returnRemoveHypan(data))
    Sector_ID = []

    for line in lines:
        checkSum,  name  = returnSplitData(line)
        name_value = (returnSetCheckLetters(name))
        print(returnMulti(name_value, name) + returnSingles(name_value, name))
        door_name = returnMakeString(returnMulti(name_value, name) + returnSingles(name_value, name))
        if checkSum == door_name:
            colour =  GREEN_BG 
            Sector_ID.append(int(returnIDNum(line)))
        else:    
            colour =  RESET 
            
        print(f"{colour}{line}{RESET}")
    print(f"The Answer is {GREEN_BG}{sum(Sector_ID)}{RESET}")



    

def part2(data):
    """Solve problem two."""

    lines = (returnReplaceHypan(data))
    Sector_ID = []

    for line in lines:
        checkSum,  name  = returnSplitData(line)
        name_value = (returnSetCheckLetters(name))
        #print(returnMulti(name_value, name) + returnSingles(name_value, name))
        door_name = returnMakeString(returnMulti(name_value, name) + returnSingles(name_value, name))
        Sector_ID = (int(returnIDNum(line)))



        print(shiftCipher(name[:-3], (Sector_ID)))

if __name__ == "__main__":
    # Execute both parts
    #answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)



#not7601