''' This is Day 6 '''
import re
import time

YEAR = 2015
DAY = 6

with open(f'/Users/MattClarke/repo/Advent of Code/AoC/AdventOfCode/AdventOfCode/AoC_2015/2015_Day_6/data.txt', 'r', encoding="utf-8") as file:
    data = file.read().strip()  # read file, and strip -- remove any white space

with open(f'/Users/MattClarke/repo/Advent of Code/AoC/AdventOfCode/AdventOfCode/AoC_2015/2015_Day_6/test_data.txt', 'r', encoding="utf-8") as file:
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


def parse_instructions(data):
    """
    Parse the input data into actionable instructions.
    
    Args:
        data: The raw input data as a string.
    
    Returns:
        A list of instructions, each as a tuple (action, start_x, start_y, end_x, end_y).
    """
    instructions = []
    lines = data.splitlines()
    for line in lines:
        match = re.match(r"^(.*?)(\d+),(\d+) through (\d+),(\d+)$", line)
        if match:
            action = match.group(1).strip()
            start_x = int(match.group(2).strip())
            start_y = int(match.group(3).strip())
            end_x = int(match.group(4).strip())
            end_y = int(match.group(5).strip())
            instructions.append((action, start_x, start_y, end_x, end_y))
    return instructions


def count_lights_on(grid, instructions):
    """
    Apply a list of instructions to the grid and count the lights that are on.
    
    Args:
        grid: The grid representing the lights.
        instructions: A list of instructions to apply.
    
    Returns:
        The count of lights that are on.
    """
    for action, start_x, start_y, end_x, end_y in instructions:
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                if action == "turn on":
                    grid[x][y] = 1
                elif action == "turn off":
                    grid[x][y] = 0
                elif action == "toggle":
                    grid[x][y] = 1 - grid[x][y]  # Flip the value

    # Count the number of lights that are on
    return sum(row.count(1) for row in grid)


def sum_light_brightness(grid, instructions):
     """
    Apply a list of instructions to the grid and sum the brightness of all lights.
    MAX 2000000
    
    Args:
        grid: The grid representing the lights.
        instructions: A list of instructions to apply.
    
    Returns:
        The 3 of all brightness 0-2 on each light.

    turn on -- increase brigtness by 1
    turn off  -- decrease brigtness by 1
    toggle -- increase brigtness by 2
    
    """


def part1(data):
    """
    Solve part 1 of the problem.
    
    Args:
        data: The input data.

Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
After following the instructions, how many lights are lit?

Your puzzle answer was 569999.

The first half of this puzzle is complete! It provides one gold star: *
    """
    grid_size = 1000
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]  # Initialize the grid
    instructions = parse_instructions(data)  # Parse the instructions
    count_ones = count_lights_on(grid, instructions)  # Apply instructions and count lights
    print(f"Number of lights on: {count_ones}")


# Main execution with timing
if __name__ == "__main__":
    time_it(part1, data)


def part2(data):
    """Function solves problem two.

    Args:
        data: The input data.
    
--- Part Two ---
You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

turn on 0,0 through 0,0 would increase the total brightness by 1.
toggle 0,0 through 999,999 would increase the total brightness by 2000000."""
    
    grid_size = 1000
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]  # Initialize the grid
    instructions = parse_instructions(data)  # Parse the instructions
    count_ones = count_lights_on(grid, instructions) 