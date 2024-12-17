''' This is Day *** '''
import time 
from itertools import permutations

'''
Tour: ['Faerun', 'AlphaCentauri', 'Snowdin', 'Tambi', 'Tristram', 'Straylight', 'Arbre', 'Norrath', 'Faerun']
Tour Cost: 490'''

YEAR = 2015
DAY = 9
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



dist = {}
towns = set()


def part1(data):
    """Function Solves problem one."""
    lines = data.splitlines()
    for i in range(len(lines)):
        l, r = lines[i].strip().split(' = ')
        d =int(r)
        t1 ,t2 = l.split(' to ')
        dist[(t1, t2)]= d
        dist[(t2, t1)]= d
        towns.add(t1)
        towns.add(t2)

    shortest = 9999999
    for r in permutations(towns):
        z = 0
        for i in range(len(r)-1):
            z += dist[(r[i],r[i+1])]

    shortest = min(shortest, z)
    print(shortest)

def part2(data):
    """Function Solves problem two."""






if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, test_data)
    answer2 = time_it(part2, data)