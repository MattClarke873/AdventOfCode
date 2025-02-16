import time

# Terminal color codes
RED = '\033[31m'
RESET = '\033[0m'

# Constants for the year and day (customize these as needed)
YEAR = 2019
DAY = 5

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


def part1(data):
    """Function Solves problem one."""
    intcode_list = [int]
    # Step 1: Convert the data into a list of integers

    intcode_list = [int(x) for x in data.split(',')]
    
    intcode_list[1]=12
    intcode_list[2]=2
    #print(intcode_list)
    
    
    for intcode in range(0, len(intcode_list)-3, 4): 
        

        match int(intcode_list[intcode]):
            case 1:
                #add int+1 and int+2 replace int+3
                first_position_int = int(intcode_list[intcode+1])
                second_position_int = int(intcode_list[intcode+2])
                val_at_pos_1 = int(intcode_list[first_position_int])
                val_at_pos_2 = int(intcode_list[second_position_int])        
                third_position = int(intcode_list[intcode+3])
                
                intcode_list[third_position] = (val_at_pos_1 + val_at_pos_2)
                #print(intcode_list)
            case 2:
                #multiply int+1 and int+2 replace int+3
                first_position_int = int(intcode_list[intcode+1])
                second_position_int = int(intcode_list[intcode+2])
                val_at_pos_1 = int(intcode_list[first_position_int])
                val_at_pos_2 = int(intcode_list[second_position_int])        
                third_position = int(intcode_list[intcode+3])
                
                intcode_list[third_position] = (val_at_pos_1 * val_at_pos_2)
                
            case 99:
                
                print(f'Interpol has finished the value at 0 is : {RED}{intcode_list[0]}{RESET}')
                intcode_list = [int(x) for x in data.split(',')]
                
                    
            case _:
                print("something Else")

            
        

def part2(data):
    """Function Solves problem two."""
       
    intcode_list = [int]
    # Step 1: Convert the data into a list of integers

    intcode_list = [int(x) for x in data.split(',')]
    for i in range(0,1):
        for noun in range(0,100):
            for verb in range(0,100):
                intcode_list[1]=noun
                intcode_list[2]=verb
                #print(intcode_list)
                
                
                for intcode in range(0, len(intcode_list)-3, 4): 
                    

                    match int(intcode_list[intcode]):
                        case 1:
                            #add int+1 and int+2 replace int+3
                            first_position_int = int(intcode_list[intcode+1])
                            second_position_int = int(intcode_list[intcode+2])
                            val_at_pos_1 = int(intcode_list[first_position_int])
                            val_at_pos_2 = int(intcode_list[second_position_int])        
                            third_position = int(intcode_list[intcode+3])
                            
                            intcode_list[third_position] = (val_at_pos_1 + val_at_pos_2)
                            #print(intcode_list)
                        
                        case 2:
                            #multiply int+1 and int+2 replace int+3
                            first_position_int = int(intcode_list[intcode+1])
                            second_position_int = int(intcode_list[intcode+2])
                            val_at_pos_1 = int(intcode_list[first_position_int])
                            val_at_pos_2 = int(intcode_list[second_position_int])        
                            third_position = int(intcode_list[intcode+3])
                            
                            intcode_list[third_position] = (val_at_pos_1 * val_at_pos_2)

                        case 3:
                            pass

                        case 4:
                            pass

                        case 99:
                            if intcode_list[0] == 19690720:
                                print(f'Interpol has finished the value at 0 is : {intcode_list[0]}')
                                print(f'The Noun = {noun} the Verb = {verb}, the Answer = \033[31m{100 * noun + verb}\033[0m ')
                                intcode_list = [int(x) for x in data.split(',')]
                            else:
                                intcode_list = [int(x) for x in data.split(',')]
                                
                        case _:
                            print("something Else")




if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)