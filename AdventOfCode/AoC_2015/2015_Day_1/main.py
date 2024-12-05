# This is Day 1
with open('myenv/AdventOfCode/AoC_2015/2015_Day_1/data.txt', 'r') as file:
    data = file.read()

def What_Floor():
    floor = 0
    for i in range(len(list(data))):
        if list(data)[i] == "(":
            floor += 1
        elif list(data)[i] == ")":
            floor -= 1
            if floor == -1:
                print(f'The Basement position is {i+1}')
                break

    print(f'the present is on floor {floor}')



What_Floor()