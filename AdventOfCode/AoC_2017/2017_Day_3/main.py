''' This is Day *** '''
import time 
from collections import defaultdict


YEAR = 2017
DAY = 3
with open(f'AdventOfCode/AoC_{YEAR}/{YEAR}_Day_{DAY}/data.txt', 'r', encoding="utf-8") as file:
    data = file.read().strip()  # read file, and strip -- remove any white space

with open(f'AdventOfCode/AoC_{YEAR}/{YEAR}_Day_{DAY}/test_data.txt', 'r', encoding="utf-8") as file:
    test_data = file.read().strip()  # read file, and strip -- remove any white space    


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



def part1(data):
    """Function Solves problem one."""
    layer = 0
    while (2 * layer + 1)**2 < int(data):
        layer += 1
    print(f'the layer is: {layer}')

    max_val_lay = (2*layer +1)**2
    print(f'The square val of this layer is: {max_val_lay} (bottom right corner)')


    steps_back= max_val_lay - int(data)
    print(f'steps from data to sqr of layer {steps_back}')
    side_length = 2 * layer + 1
    print(f'side length is {side_length}')

    side_position = steps_back % side_length  # Position along the current side
    x, y = 0, 0
    if steps_back < side_length:  # Bottom side
        x = layer
        y = -layer + side_position
    elif steps_back < 2 * side_length:  # Left side
        x = layer - (side_position + 1)
        y = -layer
    elif steps_back < 3 * side_length:  # Top side
        x = -layer
        y = -layer + (side_position + 1)
    else:  # Right side
        x = -layer + (side_position + 1)
        y = layer

    print(x, y)
    print(f'result for part 1 is {abs(x) + abs(y)}')

def part2(data):
    """Function Solves problem two."""

    grid = defaultdict(int)
    grid[(0,0)] = 1




if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)



