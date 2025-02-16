import time

# Terminal color codes
RED = '\033[31m'
RESET = '\033[0m'

# Constants for the year and day (customize these as needed)
YEAR = 2019
DAY = 4

# File paths
data_file = f'/Users/MattClarke/repo/Advent of Code/AoC/AdventOfCode/AdventOfCode/AoC_{YEAR}/{YEAR}_Day_{DAY}/data.txt'
test_data_file = f'/Users/MattClarke/repo/Advent of Code/AoC/AdventOfCode/AdventOfCode/AoC_{YEAR}/{YEAR}_Day_{DAY}/test_data.txt'

# # Read the main data file
with open(data_file, 'r', encoding="utf-8") as file:
    data = file.read().strip()  # Read and strip whitespace

# Read the test data file
with open(test_data_file, 'r', encoding="utf-8") as file:
    test_data = file.read().strip()  # Read and strip whitespace

def get_data():
    return list(range(240298, (784956+1)))  # Generate a list from the range
    

def greater_than_6(password):
    passed = False
    if password > 99999:
        passed = True
    return passed

def adjacent_match_part1(password):   
    passed = False
    password_str = str(password)
    for char in range(len(password_str)-2):
        if password_str[char] == password_str[char+1] and password_str[char] != password_str[char+2]:
            passed = True
    return passed


def adjacent_match_part2(password):
    """
    Check if the password contains at least one pair of adjacent matching digits
    that is not part of a larger group.
    """
    from collections import Counter
    password_str = str(password)

    # Count occurrences of each digit
    counts = Counter(password_str)

    # Check if there is any digit that appears exactly twice
    for digit, count in counts.items():
        if count == 2:
            return True

    return False
        
        
def greater_than(password):
    passed = False
    password_str = str(password)
    for char in range(len(password_str)-1):
        if password_str[char] <= password_str[char+1]:
            passed = True
        else:
            passed = False
            break
    return passed
    

def part1(data):
    """Solve problem one."""
    approved=[]
    passwords = get_data()
    for password in passwords:
        a = greater_than_6(password)
        b = adjacent_match_part1(password)
        c = greater_than(password)
        if a and b and c:
            approved.append(password)
    print(f"Part 1: {len(approved)} passwords meet the initial criteria.")

def part2(data):
    """Solve problem two."""
    pass  # Add the logic for part 2 here
    
    approved = []
    passwords = get_data()
    for password in passwords:
        # Adjust the adjacent_match function for stricter criteria
        if greater_than_6(password) and adjacent_match_part2(password) and greater_than(password):
            approved.append(password)
    print(f"Part 2: {len(approved)} passwords meet the stricter criteria.")




part1(data)
part2(data)
    