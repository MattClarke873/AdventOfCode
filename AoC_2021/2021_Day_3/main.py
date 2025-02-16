# Terminal color codes
RED = '\033[31m'
RESET = '\033[0m'



import os
import time
from collections import Counter


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





def find_common(lines:list,position:int, mode:str):
    common = []
    for line in lines:
        common.append(line[position])
    counter = Counter(common)
    most_common_num, count = counter.most_common(1)[0]
    if count == len(lines)/2:
        if mode == 'oxygen':
            return "1"
        if mode == 'C02':
            return "0"
    else:
        if mode == 'oxygen':
            return str(most_common_num)
        if mode == 'C02':
            return '1' if str(most_common_num) == '0' else '0'
            

def reverse_common(common_list):
    reverse_common = []
    for i in common_list:
        if i == '0':  # Compare as string
            new_i = '1'
        elif i == '1':
            new_i = '0'
        reverse_common.append(new_i) 
    return reverse_common 

def concat_list(list:list):
    return ''.join(list)


def remove_items(data_list:list, position:int, most_common_num:str):
    new_list = []
    for line in range(len(data_list)):
        if data_list[line][position] == most_common_num:
            new_list.append(data_list[line])
    return new_list


def part1(data):

    lines = data.splitlines()
    length = len(lines[0])
    
    common = []
    for i in range(length):
        common_item = find_common(lines,i, 'oxygen')
        common.append(common_item)
    

    common_cat = concat_list(common)
    common_cat_int= int(common_cat,2)
    print(common)
    print(common_cat)
    print(common_cat_int)

    common_reverse = (reverse_common(common))
    common_reverse_cat = concat_list(common_reverse)
    common_reverse_cat_int= int(common_reverse_cat,2)
    print(common_reverse)
    print(common_reverse_cat)
    print(common_reverse_cat_int)

    print(common_cat_int*common_reverse_cat_int)
    




def part2(data):
    print("part2\n")
    lines = data.splitlines()
    length = len(lines[0])
    
    
    # Oxygen default 1
    #print(len(lines))
    for i in range(0,length):
        #print(f'Part 1 round {i+1} started')
        common_item = find_common(lines, i, 'oxygen')
        new_list = remove_items(lines, i,common_item)
        lines = new_list
       # print(len(new_list))
    oxygen = int(new_list[0],2)

    # C02 default 1
    lines = data.splitlines()
    new_list = lines
    #print(len(lines))
    i =0
    
    while len(new_list) >1 :
        #print(f'Part 2 round {i+1} started')

        common_item = find_common(new_list, i, 'C02')
        new_list = remove_items(lines, i,common_item)
        lines = new_list
        #print(len(new_list))
        i += 1
    C02 = int(new_list[0],2)
    print(f'oxygen * C02 = {oxygen * C02}')



part1(data)
print('\n\n\n')
part2(data)
