''' This is Day *** '''
import time 
import pprint



YEAR = 2018
DAY = 2
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
    
    lines = data.splitlines()
    size = len(lines)
    
    for line in range(len(lines)):
        matches = 0
        answer = ''
        print(f'----------{lines[line]}------------')  
        for letter in range(len(lines[line])):
            check = lines[line][letter]
            #print(f'checking == {check}')
            for letterSec in range(len(lines[line])-1):
                checksum = lines [line][letterSec+1]
                if check == checksum and letterSec+1 != letter:
                    answer = check
                    matches +=1
        print(answer)
        print(f'matches for the word = {matches}')



def part2(data):
    """Function Solves problem two."""




if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, test_data)
    answer2 = time_it(part2, data)