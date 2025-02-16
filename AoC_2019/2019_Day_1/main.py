''' This is Day *** '''
import time 
import math


YEAR = 2019
DAY = 1
with open(f'/Users/MattClarke/repo/Advent of Code/AoC/AdventOfCode/AdventOfCode/AoC_{YEAR}/{YEAR}_Day_{DAY}/data.txt', 'r', encoding="utf-8") as file:
    data = file.read().strip()  # read file, and strip -- remove any white space

with open(f'/Users/MattClarke/repo/Advent of Code/AoC/AdventOfCode/AdventOfCode/AoC_{YEAR}/{YEAR}_Day_{DAY}/test_data.txt', 'r', encoding="utf-8") as file:
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

    base_fuel = 0
    fuel_fuel = 0
    """Function Solves problem one."""
    lines = data.splitlines()

    for line in range(len(lines)):
        
        div = int(lines[line])/3
        round_down = math.floor(div)
        fuel = round_down-2
        base_fuel+= fuel
        

        extra_fuel = fuel 
        while extra_fuel > 0:
            div_extra_fuel = extra_fuel/3
            round_down_extra_fuel = math.floor(div_extra_fuel)
            extra_fuel = round_down_extra_fuel-2

            if extra_fuel < 0:
                extra_fuel = 0
            
            fuel_fuel += extra_fuel
    print(f'Base fuel required is {base_fuel} units for')   
    print(f'Fuel required for module plus extra fuel is {fuel_fuel+base_fuel} units')


def part2(data):
    """Function Solves problem two."""




if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)