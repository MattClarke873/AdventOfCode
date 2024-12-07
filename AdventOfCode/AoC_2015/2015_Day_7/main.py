''' This is Day *** '''
import time 




YEAR = 2015
DAY = 7

with open(f'/Users/MattClarke/repo/Advent of Code/AoC/AdventOfCode/AdventOfCode/AoC_2015/2015_Day_7/data.txt', 'r', encoding="utf-8") as file:
    data = file.read().strip()  # read file, and strip -- remove any white space

with open(f'/Users/MattClarke/repo/Advent of Code/AoC/AdventOfCode/AdventOfCode/AoC_2015/2015_Day_7/test_data.txt', 'r', encoding="utf-8") as file:
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


def part1():
    """Function Solves problem one."""
    print(data)

# # Main execution with timing
# if __name__ == "__main__":
#     time_it(part1, data)


def part2():
    """Function Solves problem two."""


