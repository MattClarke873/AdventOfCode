import os
import time

# Terminal color codes
RED = '\033[31m'
RESET = '\033[0m'



# Get the absolute path of the current script
script_path = os.path.abspath(__file__)
# Get the folder where the script is saved
script_folder = os.path.dirname(script_path)
# Extract just the last folder name

file_path = os.path.join(script_folder, 'test_data.txt')

# Check if the file exists
if not os.path.isfile(file_path):
    # Create the file if it doesn't exist
    with open(file_path, 'w') as file:
        file.write('')



last_folder = os.path.basename(script_folder)
# Extract year and day
YEAR = int(last_folder.split('_')[0])  # Extract the part before the first '_'
DAY = int(last_folder.split('_')[-1])  # Extract the part after the last '_'
# File paths
data_file = f'/Users/MattClarke/repo/Advent of Code/AoC/AdventOfCode/AdventOfCode/AoC_{YEAR}/{YEAR}_Day_{DAY}/data.txt'
test_data_file = f'/Users/MattClarke/repo/Advent of Code/AoC/AdventOfCode/AdventOfCode/AoC_{YEAR}/{YEAR}_Day_{DAY}/test_data.txt'

# Read the main data file
with open(data_file, 'r', encoding="utf-8") as file:
    data = file.read().strip()  # Read and strip whitespace

# Read the test data file
with open(test_data_file, 'r', encoding="utf-8") as file:
    test_data = file.read().strip()  # Read and strip whitespace

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


def real_hands(hand):
        if hand[0] == "A":
            them = "ROCK"
        if hand[0] == "B":
            them = "PAPER"
        if hand[0] == "C":
            them = "SCISSORS"

        if hand[2] == "X":
            me = "ROCK"
            pick_score = 1
        if hand[2] == "Y":
            me = "PAPER"
            pick_score = 2
        if hand[2] == "Z":
            me = "SCISSORS"
            pick_score = 3
        return them, me, pick_score
        
    #X means you need to lose, 
    # Y means you need to end the round in a draw, and 
    # Z means you need to win.
def fixed_hands(hand):
        if hand[0] == "A":
            them = "ROCK"
        if hand[0] == "B":
            them = "PAPER"
        if hand[0] == "C":
            them = "SCISSORS"

        if hand[2] == "X":
            result = "LOSE"
            result_score = 0
        if hand[2] == "Y":
            result = "DRAW"
            result_score = 3
        if hand[2] == "Z":
            result = "WIN"
            result_score = 6
        return them, result , result_score

def losing_hand(result, them):
        #X means you need to lose, 
        # Y means you need to end the round in a draw, and 
        # Z means you need to win.
    
        #   WIN
        if result == "WIN":
            if them == "ROCK"    : me = "PAPER"
            if them == "PAPER"   : me = "SCISSORS"
            if them == "SCISSORS": me ="ROCK"
              
        #   LOSE
        if result == "LOSE":
            if them == "ROCK"    : me ="SCISSORS"
            if them == "PAPER"   : me = "ROCK"
            if them == "SCISSORS": me = "PAPER"
        # DRAW
        elif result == 'DRAW':
            me = them

        return me


def part1(data):
    """Solve problem one."""
    hands = data.splitlines()
    pick_score = 0
    pick_score_list = []
    result_score = 0
    result_score_list = [] 
    for hand in hands:
        them, me, pick_score = real_hands(hand)
        #   I WIN
        if (them == "ROCK" and me == "PAPER") or (them == "PAPER" and me == "SCISSORS") or (them == "SCISSORS" and me == "ROCK"):
            result_score = 6
            result = "win"
            
        #   THEY WIN
        if (them == "ROCK" and me == "SCISSORS") or (them == "PAPER" and me == "ROCK") or (them == "SCISSORS" and me == "PAPER"):
            result_score = 0
            result = "lose"
        #   DRAW
        elif them == me:
            result_score = 3
            result = "draw"
        


        #print(f'{them:>10} - {me:<10} : you {result:<4}:{result_score} running score:{pick_score:<10} total = {result_score + pick_score}')
        pick_score_list.append(pick_score)
        result_score_list.append(result_score)
    print(f'Hand score + results = {sum(result_score_list) + sum(pick_score_list)}')


def part2(data):
    """Solve problem two."""
    hands = data.splitlines()
    pick_score = 0
    pick_score_list = []
    result_score = 0
    result_score_list = [] 
    for hand in hands:
        them, result , result_score = fixed_hands(hand)

        me = losing_hand(result, them)

        if me == "ROCK": pick_score = 1
        if me == "PAPER": pick_score = 2
        if me == "SCISSORS": pick_score = 3
        


        print(f'{them:>10} - {me:<10} : you {result:<4}:{result_score} running score:{pick_score:<10} total = {result_score + pick_score}')
        pick_score_list.append(pick_score)
        result_score_list.append(result_score)
    print(f'Hand score + results = {sum(result_score_list) + sum(pick_score_list)}')

if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)
