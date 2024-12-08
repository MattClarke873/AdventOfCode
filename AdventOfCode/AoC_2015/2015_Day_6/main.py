''' This is Day 6 '''
import re



YEAR = 2015
DAY = 6
with open(f'AoC/AdventOfCode/AdventOfCode/AoC_{YEAR}/{YEAR}_Day_{DAY}/data.txt',
          'r',
          encoding="utf-8") as file:
    data = file.read().strip() #read file, and strip -- remove any white space

with open(f'AoC/AdventOfCode/AdventOfCode/AoC_{YEAR}/{YEAR}_Day_{DAY}/test_data.txt',
          'r',
          encoding="utf-8") as file:
    test_data = file.read().strip()  # read file, and strip -- remove any white space



def part1(data):
    """Function Solves problem one."""
# if turn on = 1
# if turn off = 0
# toggle = if 1 then = 0 and if 0 then = 1
    action=[]
    start_range_x=[]
    start_range_y=[]
    end_range_x=[]
    end_range_y=[]
    grid_size = 5
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    

    instruction = data.splitlines()
    
    for i in range(len(instruction)):
        match = re.match(r"^(.*?)(\d+),(\d+) through (\d+),(\d+)$", instruction[i])
        if match:
            action.append(match.group(1).strip())  # Everything up to the first number)
            start_range_x.append(int(match.group(2).strip())) # First coordinate pair as integers
            start_range_y.append(int(match.group(3).strip())) # First coordinate pair as integers
            
            end_range_x.append(int(match.group(4).strip())) # Second coordinate pair as integers
            end_range_y.append(int(match.group(5).strip())) # Second coordinate pair as integers
            
            # print(f'{action[i]:<15} {str(start_range[i]):<15} {str(end_range[i]):<15}')    


        range_x = end_range_x[i] - start_range_x[i]
        range_y = end_range_y[i] - start_range_y[i]



    if action[i] == "turn on":
        for x in range(range_x + 1):  # Include the endpoint
            for y in range(range_y + 1):
                grid[x + start_range_x[i]][y + start_range_y[i]] = 1
    for line in range(len(grid)):
        print(grid[line])
    print()
    
    if action[i] == "turn off":
        for x in range(range_x + 1):  # Include the endpoint
            for y in range(range_y + 1):
                grid[x + start_range_x[i]][y + start_range_y[i]] = 0
    for line in range(len(grid)):
        print(grid[line])

    
             
        # if action[i]== "turn off":
        #     print('bongo')
        # if action[i]== "toggle":
        #     print('switch')



def part2():
    '''Function Solves problem two.'''


part1(test_data)
