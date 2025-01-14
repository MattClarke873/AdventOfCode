''' This is Day *** '''
import time 
import re

import numpy as np
import pprint
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
    guard_id_dict = {}
    sleepiest_min_dict = {}
    guard_sleep_times = defaultdict(int)  # Dictionary to track total sleep time per guard
    guard_id = None  # Current guard on duty

    mins_total= []

    ####pprint.pprint(sorted_log_dict)
    

    for log in range(len(sorted_items)):
        #print(sorted_items[log][0],sorted_items[log][1]) #print the first half of the line and the second part 
        pattern = (r'Guard #(\d+) begins shift')                #set pattern from input data, (\d+) is a digit of sum sort
        match = re.search(pattern, sorted_items[log][1])        #engage the matching side, "pattern", check against "sorted_items" 
        if match:                                               # If there is a match the group 1 in the first bracketed item, assign to value
            guard_id = int(match.group(1))  
        if sorted_items[log][1] == "falls asleep":            # if no number check what string we have, if fall sleep add a sleep start time 
            sleep_start = int(sorted_items[log][0][14:])  
            #print(f'Guard {guard_id} sleeps at {sleep_start} mins') 
        if sorted_items[log][1] == "wakes up":                # if not number check what string we have, if wake up set a wake up time
            sleep_end = int(sorted_items[log][0][14:])
            #print(f'Guard {guard_id} awakes at {sleep_end} mins')
            duration = sleep_end - sleep_start                  # wake up time - sleep time gives duration of sleep
            #print(duration)
            if guard_id in guard_id_dict:   
                guard_id_dict[guard_id] += duration  # Update existing guard's sleep time
            else:
                guard_id_dict[guard_id] = duration  # Add new guard with sleep time
            


    sleepiest_guard = max(guard_id_dict, key=guard_id_dict.get)
    sleepiest_guard_sleep_duration = guard_id_dict[sleepiest_guard]

    print(f'Guard #{sleepiest_guard} spent the most minutes asleep, a total of {sleepiest_guard_sleep_duration} minutes')
    sleep_start2 = 0
    sleep_end2 = 0
    
    for log in range(len(sorted_items)):
        #print(sorted_items[log][0],sorted_items[log][1]) #print the first half of the line and the second part 
        pattern = (r'Guard #(\d+) begins shift')                #set pattern from input data, (\d+) is a digit of sum sort
        match = re.search(pattern, sorted_items[log][1])        #engage the matching side, "pattern", check against "sorted_items" 
        if match:                                               # If there is a match the group 1 in the first bracketed item, assign to value
            guard_id2 = int(match.group(1)) 
            
            #print(guard_id2) 
        elif sorted_items[log][1] == "falls asleep":            # if no number check what string we have, if fall sleep add a sleep start time 
            sleep_start2 = int(sorted_items[log][0][14:])  
            #print(f'Guard {guard_id} sleeps at {sleep_start} mins') 
        elif sorted_items[log][1] == "wakes up":                # if not number check what string we have, if wake up set a wake up time
            sleep_end2 = int(sorted_items[log][0][14:])
            #print(f'Guard {guard_id} awakes at {sleep_end} mins')
        
            
        
            for mins in range(sleep_start2, sleep_end2):
                    if guard_id2 not in sleepiest_min_dict:
                        sleepiest_min_dict[guard_id2] = {}

                    if mins in sleepiest_min_dict[guard_id2]:   
                        sleepiest_min_dict[guard_id2][mins] += 1  # Update existing guard's sleep time
                    else:
                        sleepiest_min_dict[guard_id2][mins] = 1  # Add new guard with sleep time

                    
    
    
        
    

    # Sort the inner dictionaries by their values (1, 2, 3...)
    for guard_id, mins_dict in sleepiest_min_dict.items():
    # Sort the inner dictionary based on the value
        sorted_min_dict = dict(sorted(mins_dict.items(), key=lambda x: x[1], reverse=True))  # Reverse to have larger values first
        sleepiest_min_dict[guard_id] = sorted_min_dict

    # Now my_dict is sorted based on the inner dictionary values
    



    if sleepiest_guard in sleepiest_min_dict:
        # Find the highest value in the inner dictionary for the sleepiest guard
        highest_value_sleepiest_guard = max(sleepiest_min_dict[sleepiest_guard].values())  # Get the maximum value in the inner dictionary
        # Find the minute(s) associated with the highest value
        minutes_with_highest_value_sleepiest_guard = [minute for minute, value in sleepiest_min_dict[sleepiest_guard].items() if value == highest_value_sleepiest_guard]
        
        # Convert list of minutes into a space-separated string
        minutes_str = ' '.join(map(str, minutes_with_highest_value_sleepiest_guard))

        # Print the results
        print(f"Guard {sleepiest_guard} was asleep most during minute(s) {minutes_str} on {highest_value_sleepiest_guard} days")

        print(f'the answer is ---> {sleepiest_guard*int(minutes_str)}')

        


    highest_value = -1
    associated_key = None

    # Loop through the outer dictionary
    for guard_id, mins_dict in sleepiest_min_dict.items():
        # Find the highest value in the inner dictionary
        inner_max_value = max(mins_dict.values())  # Get the maximum value in the inner dictionary
        if inner_max_value > highest_value:
            highest_value = inner_max_value
            associated_key = (guard_id, [key for key, value in mins_dict.items() if value == highest_value])  # Store the associated key (minute)
    minutes = ' '.join(map(str, associated_key[1]))
    # Print the highest value and the associated key
    print(f"Highest value: {highest_value}, Associated Guard: #{associated_key[0]}, Minute(s): {minutes}")
    print (associated_key[0]*int(minutes))
    
def part2(data):
    """Function Solves problem two."""




if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)