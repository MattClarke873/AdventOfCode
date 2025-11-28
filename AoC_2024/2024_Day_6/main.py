"""
Advent of Code Template

Provides reusable utilities for solving daily challenges.
"""

from __future__ import annotations

import os
import time
from pprint import pprint
from pathlib import Path
from typing import Callable, Any, Tuple


# ─── Terminal Color Codes ──────────────────────────────────────────────────────
color = {
    "black"         : "\033[30m",
    "blue"          : "\033[34m",
    "bold"          : "\033[1m",
    "bold_res"      : "\033[22m",
    "cyan"          : "\033[36m",
    "green"         : "\033[32m",
    "italics"       : "\033[3m",
    "italics_res"   : "\033[23m",
    "purple"        : "\033[35m",
    "red"           : "\033[31m",
    "reset"           : "\033[0m",
    "underline"     : "\033[4m",
    "underline_res" : "\033[24m",
    "white"         : "\033[37m",
    "yellow"        : "\033[33m"
}


# ─── File Handling ─────────────────────────────────────────────────────────────
def get_file_paths() -> Tuple[int, int, Path, Path, str, str]:
    """
    Retrieve the script's directory, extract the year and day from its folder name,
    ensure `test_data.txt` exists, and read input data.

    Returns:
        tuple: (YEAR, DAY, data_file, test_data_file, data, test_data)
    """
    script_folder = Path(__file__).resolve().parent
    last_folder = script_folder.name

    try:
        year = int(last_folder.split("_")[0])
        day = int(last_folder.split("_")[-1])
    except (ValueError, IndexError) as e:
        raise ValueError(
            f"Folder name '{last_folder}' must contain 'YEAR' and 'DAY' (e.g., '2018_Day_04')."
        ) from e

    data_file = script_folder / "data.txt"
    test_data_file = script_folder / "test_data.txt"

    if not test_data_file.exists():
        test_data_file.write_text("", encoding="utf-8")

    data = data_file.read_text(encoding="utf-8").strip()
    test_data = test_data_file.read_text(encoding="utf-8").strip()

    return year, day, data_file, test_data_file, data, test_data


# ─── Utility ───────────────────────────────────────────────────────────────────
def time_it(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
    """
    Measure the execution time of a function.

    Args:
        func: The function to time.
        *args: Positional arguments for the function.
        **kwargs: Keyword arguments for the function.

    Returns:
        Any: The function's return value.
    """
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    elapsed_time = time.perf_counter() - start_time
    print(f"{func.__name__} executed in {elapsed_time:.6f} seconds")
    return result


def get_grid(data):
    """Take the data and turn it in to a gird, then return the grid and number of rows/cols"""
    lines = data.splitlines()
    grid = [list(line) for line in lines]
    return grid


def find_start(grid):
    for row_id, row in enumerate(grid):
        for col_id, char in enumerate(row):
            if char == "^":
                return row_id, col_id  # return instead of just print


def get_moving(start, grid):
    # start moving UP (row -1) if `.`` keep moving until hit a "#" then direction = RIGHT else if outside of grid END
    # start moving RIGHT (col +1) if ``.` keep moving until hit a  "#" then direction = DOWN else if outside of grid END
    # start moving DOWN (row +1) if `.` keep moving until hit a "#" then direction = LEFT else if outside of grid END
    # start moving LEFT (col -1) if `.` keep moving until hit a "#"  then direction = UP else if outside of grid END

    row, col = start
    direction = 'UP'
    
    while 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        match direction:
            case "UP":
                if row - 1 >= 0:
                    if grid[row - 1][col] != "#":  
                        row -= 1
                        print(f"we are moving {direction} {[row],[col]}.")
                    else:
                        direction = "RIGHT"
                        print(f'Turning {direction}')
                else:
                    print(f"I think we are at the end {[row],[col]} (Up)")
                    print("out of range")
                    break
            
            case "RIGHT":
                if col + 1 < len(grid[0]):
                    if grid[row][col + 1] != "#":
                        col += 1
                        print(f"we are moving {direction} {[row],[col]}.")
                    else:
                        print(f"I think we are at the end {[row],[col]} (Right)")
                        direction = "DOWN"
                else:
                    print(f"I think we are at the end {[row],[col]} (Right)")
                    print("out of range")
                    break
            
            case "DOWN":
                if row + 1 < len(grid):
                    if grid[row + 1][col] != "#":
                        row += 1
                        print(f"we are moving {direction} {[row],[col]}.")
                    else:
                        print(f"I think we are at the end {[row],[col]} (Down)")
                        direction = "LEFT"
                else:
                    print(f"I think we are at the end {[row],[col]} (Down)")
                    print("out of range")
                    break
            
            case "LEFT":
                if col - 1 >= 0:
                    if grid[row][col - 1] != "#":
                        col -= 1
                        print(f"we are moving {direction} {[row],[col]}.")
                    else:
                        print(f"I think we are at the end {[row],[col]} (left)")
                        direction = "UP"
                else:
                    print(f"I think we are at the end {[row],[col]} (left)")
                    print("out of range")
                    break
            
            
            case _:
                print("Something's not right.")
    else:
        print("Starting position is outside the grid!")





# ─── Puzzle Solutions ──────────────────────────────────────────────────────────

def part1(data: str) -> Any:
    """Solve problem one."""
    grid = get_grid(data)
    start = find_start(grid)
    get_moving(start, grid)


def part2(data: str) -> Any:
    """Solve problem two."""
    # TODO: implement solution
    return None


# ─── Entry Point ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    YEAR, DAY, data_file, test_data_file, data, test_data = get_file_paths()

    print(f"{color['bold']}{color['green']}Running Advent of Code {YEAR}, Day {DAY}{color['reset']}")
    

    answer1 = time_it(part1, data)
    if answer1 == None:
        colorRule = f"{color['bold']}{color['red']}"
    else:
        colorRule = f"{color['bold']}{color['green']}"
    print(f"Part 1 Answer: {colorRule}{answer1}{color['reset']}")

    answer2 = time_it(part2, data)
    if answer2 == None:
        colorRule = f"{color['bold']}{color['red']}"
    else:
        colorRule = f"{color['bold']}{color['green']}"
    print(f"Part 2 Answer: {colorRule}{answer2}{color['reset']}")

