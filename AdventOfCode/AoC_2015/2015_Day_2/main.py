"""Day 2 of AoC 2015."""


from mytools.colors import RED, RESET, CYAN
from mytools import PrintList


with open('myenv/AdventOfCode/AoC_2015/2015_Day_2/data.txt', 'r', encoding="utf-8") as file:
    data = file.read()


def Wrapping_Paper():
    l = []
    w = []
    h = []
    boxes = data.splitlines()  # Split each line in to a new element

    for index, box in enumerate(boxes):
        split_data = box.split('x')  # Boxes items will be 123 X 456 X 789
        l.append(split_data[0])  # first segment (123)
        w.append(split_data[1])  # Second segment (456)
        h.append(split_data[2])  # Third segment (789)



    area = []
    for i in range(len(boxes)):
        area.append(2*int(l[i])*int(w[i])+(2*int(w[i])*int(h[i]))+(2*int(h[i])*int(l[i])))

    print(f'the area of the wrapping paper needed is: {RED}{sum(area)}{RESET} SqFt')
    extra = []

    for i in range(len(l)):
        extra.append([int(l[i]), int(w[i]), int(h[i])])
    
    spare = []
    for i in extra:
        spare.append(sorted(i))

        SpareArea= []
    for i in range(len(boxes)):
        SpareArea.append((2*int(l[i])*int(w[i]))+(2*int(w[i])*int(h[i]))+(2*int(h[i])*int(l[i]))+(spare[i][0]*spare[i][1]))
    
    print(sum(SpareArea))
    
    ribbon = []
    for i in range(len(spare)):
        ribbon.append((spare[i][0] + spare[i][0]+ spare[i][1]+spare[i][1])+(spare[i][0]*spare[i][1]*spare[i][2]))
    print(sum(ribbon))

Wrapping_Paper()
