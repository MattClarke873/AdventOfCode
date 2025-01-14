''' This is Day *** '''
import time 



YEAR = 2018
DAY = 5
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
    data_list=[]
    for i in data:
        data_list.append(i)

    i = 0
    while i < len(data_list) - 1:
        first = data_list[i]
        second = data_list[i + 1]

        # Check if they react
        if first != second and first.upper() == second.upper():
            print(f"Reacting: {first} and {second}")
            del data_list[i]       # Remove the first element
            del data_list[i]       # Remove the second element (at the same index after deletion)
            i = max(i - 1, 0)      # Move one step back to recheck the new adjacent pair
        else:
            i += 1  # Move to the next character
    result =  data_list


    
    print("Resulting polymer:", "".join(result))
    print("Length of resulting polymer:", len(result))
        


 

         

def part2(data):
    """Function Solves problem two."""




if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)