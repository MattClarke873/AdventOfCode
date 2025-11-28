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









bank_lists = []

def first_bank(data):
    global bank_lists
    """Add list of numbers into a list
    i will check later if the output list is in the bigger list of lists."""
    banks = [int(x) for x in data.strip().split()]
    bank_lists.append(banks.copy())
    return bank_lists




bank_list_index = 0


def biggest_bank(index):
    """Find the largest bank and its index."""
    banks = bank_lists[index]
    bank = 0
    largest = 0
    index = 0
    for bank in banks:
        if bank > largest :
            largest = bank
            index = banks.index(bank)   
        elif bank == largest:
            continue
        else:
            continue
    
    return index



def share(list_index, largest_bank_index):
    """Set the big bank to zero and share the rest"""
    current_list = bank_lists[list_index].copy()
    steps = current_list[largest_bank_index]
    current_list[largest_bank_index] = 0 
    index = (largest_bank_index +1) % len(current_list)

    for _ in range(steps):      # for range of the largest index bank
        current_list[index] += 1          # add 1 to each bank
        index = (index + 1) % len(current_list)  # cycle thought each bank (wrapped)
    
    
    return current_list
    

def print_highlighted_list(lst, highlight_index):
    """Print a list, highlighting the item at highlight_index with a green background."""
    out_items = []
    for idx, val in enumerate(lst):
        if idx == highlight_index:
            out_items.append(f"{GREEN_BG}{val}{RESET}")
        else:
            out_items.append(str(val))
    print("[" + ", ".join(out_items) + "]")
    



def part1(data): 

    index = 0 
    first_bank(data)
    first = None

 
    while True:    
        lst = (share(index,biggest_bank(index)))
        if lst not in bank_lists:
            bank_lists.append(lst)
            index +=1
            #print(f"Moving Memory ..{index}", end="\r", flush=True)
            print(f"Moving Memory ..{index}", end="\r", flush=False)
            
        elif lst in bank_lists:
            index +=1
            bank_lists.append(lst)
            if first is None:
                first = index
                print(f"First match found at {first}")
                check = lst
            elif first is not None:
                if bank_lists.count(check) < 3:
                    print(f"Moving Memory for second ..{index}", end="\r", flush=False)
                elif bank_lists.count(check) > 2:
                    print(f'final index = {index} gap == {index} - {first} = {index-first} ')
                    break


def part2(data):
    pass
        
if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)
