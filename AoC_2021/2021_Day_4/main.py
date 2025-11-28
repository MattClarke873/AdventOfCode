"""
Advent of Code Template

Provides reusable utilities for solving daily challenges.
"""

from __future__ import annotations

import os
import time
import pprint as pp
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


# ─── Puzzle Solutions ──────────────────────────────────────────────────────────
def parse_call_numbers(data: str) -> Any:
    """
    Take initial data and split to call numbers
    and cards returning the call number as a list 
    and from index 1 to the end of the cards
    """

    numbers = data.split("\n\n")
    call = numbers[0].split(",") 

    return call, numbers[1:]


def sort_cards(cards: list):
    """
    Turns each card in to a list on line 
    containing a list of digits
    """
    result = []
    for card in cards:
        lines = card.strip().split("\n")  # split into lines
        card_data = []
        for line in lines:
            digits = line.strip().split()  # split each line into digits by spaces
            card_data.append(digits)
        result.append(card_data)

    return result


def part1(data: str) -> Any:
    """Solve problem one."""
    # TODO: implement solution
    call, numbers = parse_call_numbers(data)
    cards = sort_cards(numbers)

    called = []
    for i, digit in enumerate(call):
        called.append(digit)
        print(digit, i+1)
        

    return call, cards

    
    


def part2(data: str) -> Any:
    """Solve problem two."""
    # TODO: implement solution
    return None


# ─── Entry Point ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    YEAR, DAY, data_file, test_data_file, data, test_data = get_file_paths()

    print(f"{color['bold']}{color['green']}Running Advent of Code {YEAR}, Day {DAY}{color['reset']}")
    

    answer1 = time_it(part1, data)
    if answer1 is None:
        ColorRule = f"{color['bold']}{color['red']}"
    else:
        ColorRule = f"{color['bold']}{color['green']}"
    print(f"Part 1 Answer: {ColorRule}{answer1}{color['reset']}")

    answer2 = time_it(part2, data)
    if answer2 is None:
        ColorRule = f"{color['bold']}{color['red']}"
    else:
        ColorRule = f"{color['bold']}{color['green']}"
    print(f"Part 2 Answer: {ColorRule}{answer2}{color['reset']}")
