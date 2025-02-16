import time
import matplotlib.pyplot as plt

# Color codes for terminal output
RED = '\033[31m'
BLUE = '\033[34m'
RESET = '\033[0m'

# Constants for the year and day
YEAR = 2019
DAY = 3

# File paths
data_file = f'/Users/MattClarke/repo/Advent of Code/AoC/AdventOfCode/AdventOfCode/AoC_{YEAR}/{YEAR}_Day_{DAY}/data.txt'
test_data_file = f'/Users/MattClarke/repo/Advent of Code/AoC/AdventOfCode/AdventOfCode/AoC_{YEAR}/{YEAR}_Day_{DAY}/test_data.txt'

# Read data files
with open(data_file, 'r', encoding="utf-8") as file:
    data = file.read().strip()  # Read and strip whitespace

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



def visualize_wire_path(wire_route):
    wire_path = [(0, 0)]  # Initial position
    full_path = [(0, 0)]

    for step in wire_route:
        direction = step[0]
        distance = int(step[1:])
        x, y = wire_path[-1]
        new_positions = []
        
        match direction:
            case "U":
                new_positions = [(x, y + i) for i in range(1, distance + 1)]
            case "D":
                new_positions = [(x, y - i) for i in range(1, distance + 1)]
            case "L":
                new_positions = [(x - i, y) for i in range(1, distance + 1)]
            case "R":
                new_positions = [(x + i, y) for i in range(1, distance + 1)]
            case _:
                print(f"Invalid direction: {direction}")
                continue
        
        wire_path.extend(new_positions)
        full_path.extend(new_positions)

    return full_path

def part1(data):
    lines = data.splitlines()
    wire_1_route = [x for x in lines[0].split(',')]
    wire_2_route = [x for x in lines[1].split(',')]

    wire1 = visualize_wire_path(wire_1_route)
    wire2 = visualize_wire_path(wire_2_route)

    wire1_set = set(wire1)
    matching_tuples = list(filter(lambda x: x in wire1_set, wire2))

    if matching_tuples:
        manhat = {abs(x) + abs(y) for x, y in matching_tuples}
        print(f"Shortest Manhattan distance (excluding 0,0): {sorted(manhat)[1]}")
    else:
        print("No matching tuples found.")

    # Find matching tuples with their indices
    matches = [(i, j, val) for i, val in enumerate(wire1) for j, val2 in enumerate(wire2) if val == val2]
    
    if matches:
        for i, j, val in matches:
            print(f"Match found: {val} at index {i} in wire1 and index {j} in wire2")
    else:
        print("No matches found in part 2.")

    #return sorted(manhat)[1], wire1, wire2 # Return second smallest distance (if exists)

def part2(data):
    """Solves problem two."""
    # Add part 2 logic here


if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)
