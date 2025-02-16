''' This is Day *** '''
import time 
import re
import numpy as np
from datetime import datetime
from collections import defaultdict, Counter


YEAR = 2018
DAY = 4
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
    """Function Solves problem one."""

    lines = data.splitlines()  # Split the data into lines
    log_dict = {}  # Dictionary to store the date-time and corresponding activity

    for line in lines:
        # Print the substring that starts from index 1 to index 17 (exclusive)
        a = (line[1:17])  # This slices the string to get the date-time portion   
        b = (line[19:])  # get the action that happen at this time.

    # Add the date-time and activity to the dictionary
        log_dict[a] = b
        # Sort the dictionary by date-time (keys), converting the date-time to datetime objects
    sorted_log_dict = dict(sorted(log_dict.items(), key=lambda x: datetime.strptime(x[0], '%Y-%m-%d %H:%M')))

    sorted_items = list(sorted_log_dict.items())
    guard_list = set()
    guard_sleep_times = defaultdict(int)  # Dictionary to track total sleep time per guard
    guard = None  # Current guard on duty
    sleep_start = None
    mins_total= []


    for log in range(len(sorted_items)):
        pattern = r"Guard #(\d+) begins shift"
        match = re.search(pattern, sorted_items[log][1])
        if match:
            guard = match.group(1)
            guard_list.add(int(guard))
            #print(f'{sorted_items[log][0][14:]} #{sorted_items[log][1][11:]}')

        elif sorted_items[log][1] == "falls asleep":
            sleep_start= sorted_items[log][0][14:]
        elif sorted_items[log][1] == "wakes up": 
            sleep_end = int(sorted_items[log][0][14:])  # Track wake-up time
            sleep_time = int(sleep_end) - int(sleep_start)
            guard_sleep_times[guard] += sleep_time  # Add sleep time for the guard
            for mins in range(int(sleep_start), int(sleep_end)+1):
                    mins_total.append(mins)
            # Find the guard with the maximum sleep time
            
    sleepiest_guard = max(guard_sleep_times, key=guard_sleep_times.get)
    max_sleep_time = guard_sleep_times[sleepiest_guard]



                




    # Count occurrences of each number
    counter = Counter(mins_total)

    # Find the most common number and its count
    most_common_number, count = counter.most_common(1)[0]
    

    print(f'Guard #{sleepiest_guard} slept for {most_common_number} minutes, lazy sod')
    day4 = int(sleepiest_guard) * int(most_common_number)
    print(f'Day 4 answer is {day4}')
    #
    #not 76534
    #





def part2(data):
    """Function Solves problem two."""




if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)