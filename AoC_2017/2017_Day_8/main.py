import os
import time
import pprint as pp

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

def parse_data(line):
        '''Split each line in to 4 section 
        q inc -541 if c != 4
        {q} {inc} {-541} {if c != 4}

        {1 = Desc = q}
        {2 = Instruction = inc}
        {3 = value = -541}
        {4 = condition = if c != 4}
           '''
        parts = line.split()
        desc = str(parts[0].strip())
        instruction =  str(parts[1].strip())
        value = int(parts[2])
        condition = str(" ".join(parts[3:]))

        return desc, instruction, value, condition


def para_condition(condition):
    parts = condition.split()
    
    desc = str(parts[1].strip())
    operation = str(parts[2].strip())
    value = int(parts[3])
    return desc, operation, value


def matching_cases(desc_list ,desc, instruction, value,cond_desc, cond_operation, cond_value):
# q inc -541 if c != 4
#         

    max_value = 0

    match cond_operation:
        case '>':
            if desc_list[cond_desc]["value"] > cond_value:  #if the value in the list is > the cond_value
                if instruction == 'inc':
                    desc_list[desc]["value"] = desc_list[desc]["value"]+value    #and if inc in line increase
                    max_value = desc_list[desc]["value"]
                elif instruction == 'dec':
                    desc_list[desc]["value"] = desc_list[desc]["value"]-value    #and if dec in line decrease
                    max_value = desc_list[desc]["value"]
            else:
                #print(f"{RED}error >{RESET}")   #if the list value is not greater than cond_value pass on by
                pass
        case '<=':

            if desc_list[cond_desc]["value"] <= cond_value:
                if instruction == 'inc':
                    desc_list[desc]["value"] = desc_list[desc]["value"]+value
                    max_value = desc_list[desc]["value"]
                elif instruction == 'dec':
                    desc_list[desc]["value"] = desc_list[desc]["value"]-value
                    max_value = desc_list[desc]["value"]
                   
            else:
                #print(f"{RED}error <={RESET}")
                pass
        case '>=':

            if desc_list[cond_desc]["value"] >= cond_value:
                if instruction == 'inc':
                    desc_list[desc]["value"] = desc_list[desc]["value"]+value
                    max_value = desc_list[desc]["value"]
                elif instruction == 'dec':
                    desc_list[desc]["value"] = desc_list[desc]["value"]-value
                    max_value = desc_list[desc]["value"]
            else:
                #print(f"{RED}error >={RESET}")
                pass
        case '<':

            if desc_list[cond_desc]["value"] < cond_value:
                if instruction == 'inc':
                    desc_list[desc]["value"] = desc_list[desc]["value"]+value
                    max_value = desc_list[desc]["value"]
                elif instruction == 'dec':
                    desc_list[desc]["value"] = desc_list[desc]["value"]-value
                    max_value = desc_list[desc]["value"]
            else:
                #print(f"{RED}error <{RESET}")
                pass
        case '!=':

            if desc_list[cond_desc]["value"] != cond_value:
                if instruction == 'inc':
                    desc_list[desc]["value"] = desc_list[desc]["value"]+value
                    max_value = desc_list[desc]["value"]
                elif instruction == 'dec':
                    desc_list[desc]["value"] = desc_list[desc]["value"]-value
                    max_value = desc_list[desc]["value"]
            else:
                #print(f"{RED}error !={RESET}")
                pass
        case '==':
            if desc_list[cond_desc]["value"] == cond_value:
                if instruction == 'inc':
                    desc_list[desc]["value"] = desc_list[desc]["value"]+value
                    max_value = desc_list[desc]["value"]
                elif instruction == 'dec':
                    desc_list[desc]["value"] = desc_list[desc]["value"]-value
                    max_value = desc_list[desc]["value"]
            else:
                #print(f"{RED}error == {RESET}")
                pass
        case _:
            print(f"{RED}error OTHER CASE{RESET}")
    
    return max_value
    
        

def make_list(desc, cond_desc, desc_list):
    desc_list.setdefault(desc, {"value": 0})
    desc_list.setdefault(cond_desc, {"value": 0})



def part1(data):
    """Solve problem one."""
    desc_list = {}   # dict keyed by desc
    running_list=[]
       
    lines = data.splitlines()
    for line in lines:
        desc, instruction, value, condition = parse_data(line)
        cond_desc, cond_operation, cond_value = para_condition(condition)
        make_list(desc, cond_desc, desc_list)
    


    for line in lines:
        desc, instruction, value, condition = parse_data(line)
        cond_desc, cond_operation, cond_value = para_condition(condition)
        matching_cases(desc_list ,desc, instruction, value,cond_desc, cond_operation, cond_value)
        running_list.append(matching_cases(desc_list ,desc, instruction, value,cond_desc, cond_operation, cond_value))
    #max_key = max(desc_list, key=lambda k: desc_list[k]["value"])
    #print(max_key, desc_list[max_key]["value"])
    print(sorted(running_list))

def part2(data):
    """Solve problem two."""
    pass  # Add the logic for part 2 here

if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)
