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
    
    two_count = 0
    three_count = 0
    lines = data.splitlines()
    
    for line in lines:
        two = False
        three = False
        print(f'----------{line}------------')
        char_counts = {}
        
        # Count each character in the line
        for char in line:
            char_counts[char] = char_counts.get(char, 0) + 1
        
        # Print the counts
        for char, count in char_counts.items():
            if count == 2:
                print(f"'{char}': {count}")
                two = True    
            if count == 3:
                print(f"'{char}': {count}")
                three = True
            
        if two:
            two_count +=1 
        if three:
            three_count +=1 
              
    print(f'2 = {two_count}')
    print(f'3 = {three_count}')
    print(f'Answer = {two_count*three_count}')
    



def part2(data):
    """Function Solves problem two."""




if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)