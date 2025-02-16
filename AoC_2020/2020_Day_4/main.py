import os
import time
import re
import pprint as p

# Terminal color codes
RED = '\033[31m'
RESET = '\033[0m'

# Get the absolute path of the current script
script_path = os.path.abspath(__file__)
# Get the folder where the script is saved
script_folder = os.path.dirname(script_path)
# Extract just the last folder name
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


def sort_cred(data):
    return data.split('\n\n')
    

def split_cred_items(data: list):
    creds = []
    for line in data:
        creds.append(re.split(r'[ \n]+', line))
    return creds

def key_value(data):
    cred_dicts = []  # List to store each credential as a dictionary
    for fields in data:
        cred_dict = {item.split(':')[0]: item.split(':')[1] for item in fields if ':' in item}
        cred_dicts.append(cred_dict)
    return cred_dicts



def part1(data):
    """Solve problem one."""
    cred = (sort_cred(data))
    sorted_ids = (key_value(split_cred_items(cred)))
    valid = 0
    for ids in sorted_ids:
        if "byr" in ids and "iyr" in ids and "eyr" in ids and "hgt" in ids and "hcl" in ids and "ecl" in ids and "pid" in ids:
            valid += 1
            
    print(f'Number of valid IDs: {valid}\n\n')

    
    
    


def part2(data):
    """Solve problem two."""
    cred = (sort_cred(data))
    sorted_ids = (key_value(split_cred_items(cred)))
    valid = False
    valid_count = 0
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for ids in sorted_ids:
        if not all(field in ids for field in required_fields):
            continue
        
        
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if not (1920 <= int(ids['byr']) <= 2002):
            continue
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        if not (2010 <= int(ids['iyr']) <= 2020):
            continue
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        if not (2020 <= int(ids['eyr']) <= 2030):
            continue
            
        # hgt (Height) - a number followed by either cm or in:

        #If cm, the number must be at least 150 and at most 193.
        if ids['hgt'].endswith('cm'):
            unit_val = int(ids['hgt'][:-2])
            if not (150 <= unit_val <= 193):
                continue
        #If in, the number must be at least 59 and at most 76.
        elif ids['hgt'].endswith('in'):
            unit_val = int(ids['hgt'][:-2])
            if not (59 <= unit_val <= 76):
                continue
        else:
            continue
                
                    
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        if ids['hcl'].startswith('#') and len(ids['hcl']) == 7:
           if not re.fullmatch(r"[0-9a-f]+", ids['hcl'][1:], re.IGNORECASE):
               continue  
        else:
            continue

        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if ids['ecl'] not in eye_colors:
            continue

        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        if not (len(ids['pid']) == 9 and ids['pid'].isdigit()):
            continue

        
        valid_count +=1
    print(valid_count)



if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)
