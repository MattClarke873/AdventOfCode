''' This is Day 3'''

import hashlib as Hash

YEAR = 2015
DAY = 4
with open(f'AoC/AdventOfCode/AdventOfCode/AoC_{YEAR}/{YEAR}_Day_{DAY}/data.txt', 'r', encoding="utf-8") as file:
    data = file.read().strip()  # read file, and strip -- remove any white space


def part1(data):
    """Function Solves problem one."""
    Index = 1
    while True:
        key = data + str(Index)
        HASH = Hash.md5(key.encode('ascii')).hexdigest()
        if HASH[:5] == '00000':
            break
        Index += 1
    print(Index, key)


def part2(data):
    """Function Solves problem two."""
    Index = 1
    while True:
        key = data + str(Index)
        HASH = Hash.md5(key.encode('ascii')).hexdigest()
        if HASH[:6] == '000000':
            break
        Index += 1
    print(Index, key)



part2(data)