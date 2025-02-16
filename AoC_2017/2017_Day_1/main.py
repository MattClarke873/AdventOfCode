''' This is Day *** '''
import time
from itertools import cycle


YEAR = 2017
DAY = 1
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
    cap =0
    size = len(data)
    for i in range(size):
        #print(data[i % size], data[(i+1) % size] )

        if data[i % size] == data[(i+1) % size] :
            #print(data[i % size], data[(i+1) % size])
            cap = cap + int(data[i % size])

    print(f'sum of cap: {cap}')



def part2(data):
    """Function Solves problem two."""
    cap =0
    size = len(data)
    halfway = int((len(data)/2))
    for i in range(size):
        #print(data[i % size], data[(i+halfway) % size] )

        if data[i % size] == data[(i+halfway) % size] :
            #print(data[i % size], data[(i+halfway) % size])
            cap = cap + int(data[i % size])

    print(f'sum of cap (halfway): {cap}')



if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)