import re
from collections import defaultdict

# Read and sort data
with open('/Users/MattClarke/repo/Advent of Code/AoC/AdventOfCode/AdventOfCode/AoC_2018/2018_Day_4/test_data.txt', 'r') as file:
    logs = sorted(file.readlines())

# Regular expressions to parse the log entries
guard_re = re.compile(r"Guard #(\d+) begins shift")
time_re = re.compile(r"\[.*:(\d+)] (falls asleep|wakes up)")

# Data structures to store sleep data
guard_sleep = defaultdict(int)
minute_sleep = defaultdict(lambda: defaultdict(int))

# Parse logs and calculate sleep patterns
current_guard = None
sleep_start = None

for log in logs:
    if "Guard" in log:
        current_guard = int(guard_re.search(log).group(1))
    elif "falls asleep" in log:
        sleep_start = int(time_re.search(log).group(1))
    elif "wakes up" in log:
        sleep_end = int(time_re.search(log).group(1))
        guard_sleep[current_guard] += sleep_end - sleep_start
        for minute in range(sleep_start, sleep_end):
            minute_sleep[current_guard][minute] += 1

# Find the guard with the most minutes asleep
sleepiest_guard = max(guard_sleep, key=guard_sleep.get)
sleepiest_minute = max(minute_sleep[sleepiest_guard], key=minute_sleep[sleepiest_guard].get)

# Calculate the result
result = sleepiest_guard * sleepiest_minute
print(f"Guard ID: {sleepiest_guard}, Minute: {sleepiest_minute}, Result: {result}")
