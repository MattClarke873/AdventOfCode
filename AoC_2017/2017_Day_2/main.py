''' This is Day *** '''
import time 



YEAR = 2017
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

    total = 0 
    for line in data.splitlines():
        l = [int(x) for x in line.split()]
        diff = (max(l)-min(l))
        total = total + diff


    print(total)



def part2(data):
    """Function Solves problem two."""

    total = 0 
    for line in data.splitlines():
        l = [int(x) for x in line.split()]
        l.sort()
        done = False
        for x in l:
            if done:
                break
            for y in l:
                if x!=y and  y%x ==0:
                    total += (y/x)
                    done = True
        
    print(total)


if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)