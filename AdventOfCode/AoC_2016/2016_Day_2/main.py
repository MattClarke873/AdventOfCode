''' This is Day *** '''
import time 



YEAR = 2016
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
    """Function solves problem one."""
    # Initialize the starting position on the keypad grid
    row = 1  # Starting row index (middle row)
    digit = 1  # Starting column index (middle column)

    # Define the keypad layout as a 2D list
    key = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Initialize the passcode as an empty string
    passcode = ""

    # Iterate through each line of input instructions
    for line in data.splitlines():
        # Process each character in the current line
        for char in line:
            if char == "U":  # Move up
                row = max(0, row - 1)  # Ensure row does not go below 0 (top boundary)
            elif char == "D":  # Move down
                row = min(2, row + 1)  # Ensure row does not exceed 2 (bottom boundary)
            elif char == "L":  # Move left
                digit = max(0, digit - 1)  # Ensure digit does not go below 0 (left boundary)
            elif char == "R":  # Move right
                digit = min(2, digit + 1)  # Ensure digit does not exceed 2 (right boundary)
        # Append the digit at the current position on the keypad to the passcode
        passcode += str(key[row][digit])

    # Print the final passcode
    print(f'passcode = {passcode}')


def part2(data):
    """Function Solves problem two."""
        # Initialize the starting position on the keypad grid
    row = 2  # Starting row index (middle row)
    digit = 0  # Starting column index (middle column)

    # Define the keypad layout as a 2D list
    key = [['x', 'x',  1, 'x','x'],
           ['y',  2,   3,  4, 'y'],
           [5,    6,   7,  8,  9 ],
           ['z', "A", "B","C", 'z'],
           ['q', 'q', "D",'q','q'] ]

        # Initialize the passcode as an empty string
    passcode = ""


    # Iterate through each line of input instructions
    for line in data.splitlines():
        # Process each character in the current line
        for char in line:
            if char == "U":  # Move up
                row-=1
                if digit == 0 or digit == 4:
                    if row < 2:
                        row = 2
                if digit == 1 or digit == 3:
                    if row < 1:
                        row = 1
                if digit == 2:
                    if row < 0:
                        row = 0
            elif char == "D":  # Move down
                row+=1
                if digit == 0 or digit == 4:
                    if row > 2:
                        row = 2
                if digit == 1 or digit == 3:
                    if row > 3:
                        row = 3
                if digit == 2:
                    if row > 4:
                        row = 4
                 # Ensure row does not exceed 2 (bottom boundary)
            elif char == "L":  # Move left
                digit -=1
                if row == 0 or row == 4:
                    if digit < 2:
                        digit = 2
                if row == 1 or row ==3:
                    if digit <1:
                        digit =1
                if row ==2:
                    if digit <0:
                        digit = 0 
                

            elif char == "R":  # Move right
                digit +=1
                if row == 0 or row == 4:
                    if digit > 2:
                        digit = 2
                if row == 1 or row ==3:
                    if digit >3:
                        digit =3
                if row ==2:
                    if digit >4:
                        digit = 4 
            if key[row][digit] == 'z' or key[row][digit] == 'y' or key[row][digit] == 'x'or key[row][digit] == 'x':
                print(f"ERROR!!!!! {[row]},{[digit]} {char}")
        
        # Append the digit at the current position on the keypad to the passcode
        passcode += str(key[row][digit])

    # Print the final passcode
    print(f'passcode = {passcode}')







if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)