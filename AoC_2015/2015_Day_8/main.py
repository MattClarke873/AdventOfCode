''' This is Day *** '''
import time 



YEAR = 2015
DAY = 8
with open(f'AdventOfCode/AoC_2015/2015_Day_8/data.txt', 'r', encoding="utf-8") as file:
    data = file.read().strip()  # read file, and strip -- remove any white space

with open(f'AdventOfCode/AoC_2015/2015_Day_8/test_data.txt', 'r', encoding="utf-8") as file:
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
    """--- Day 8: Matchsticks ---"""
    code_char= 0
    string_char = 0

    lines = data.splitlines()  # Split the data into lines
    for line in lines:
        code_char += len(line)
        string_char += len(eval(line))

    print(f'code to string: {code_char-string_char}')
    

def part2(data):
    """Function Solves problem two."""
    code_char= 0
    rep_code_char = 0
    extra_char = 0

    lines = data.splitlines()  # Split the data into lines
    line_quotes = 2*len(lines)

    for line in lines:
        code_char += len(line)
        for char in line:
            if char == "\"" or char == "\\" :
                extra_char += 1
    print(f'extra char: {(extra_char + line_quotes)}')


    


if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)