''' This is Day *** '''
import time 



YEAR = 2018
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
    total = 0
    lines = data.splitlines()
    for i in range(len(lines)):
        #print(lines[i])
        value = int(lines[i])
        total += value
    print(total)


def part2(data):
    """Function solves problem two."""
    total = 0
    seen_totals = set()
    running_total = 0

    # Parse the input into a list of integers
    lines = list(map(int, data.splitlines()))

    # Continuously cycle through the data
    index = 0
    while True:
        value = lines[index % len(lines)]  # Cycle through the input data the % allows you to continuously cycle
        running_total += value

        if running_total in seen_totals:
            print(f"First repeat: {running_total}")
            return

        seen_totals.add(running_total)
        index += 1






if __name__ == "__main__":
    # Execute both parts
    ANSWER_1 = time_it(part1, data)
    ANSWER_2 = time_it(part2, data)
