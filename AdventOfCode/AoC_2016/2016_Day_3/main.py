''' This is Day *** '''
import time 



YEAR = 2016
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
    lines = data.strip().splitlines()  # Split input into individual lines and remove leading/trailing whitespace
    processed = []
    
    for line in lines:
        # Use split() to separate based on any whitespace and convert to integers
        numbers = list(map(int, line.split()))
        if len(numbers) == 3:  # Ensure there are exactly 3 integers per line
            processed.append(tuple(numbers))
        else:
            print(f"Invalid line skipped: {line}")  # Debugging for invalid lines
    
    print(processed[0][0])

    count= 0
    for i in range(len(processed)):
        if ((processed[i][0] + processed[i][1] > processed[i][2]) and (processed[i][0] + processed[i][2] > processed[i][1]) and (processed[i][1] + processed[i][2] > processed[i][0])):
            count += 1
    print(f'possilbe = {count}')


def part2(data):
    """Function Solves problem two."""




if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)