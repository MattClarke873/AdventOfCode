''' This is Day 3'''


with open('AoC/AdventOfCode/AdventOfCode/AoC_2015/2015_Day_3/data.txt', 'r', encoding="utf-8") as file:
    data = file.read()



''' 
Street i [0,0,0,0,0,0,0,0,0,0]
Street i [0,0,0,0,0,0,0,0,0,0]
Street i [0,0,0,0,0,0,0,0,0,0]
Street i [0,0,0,0,0,0,0,0,0,0]
Street i [0,0,0,0,0,0,0,0,0,0]
Street i [0,0,0,0,0,0,0,0,0,0]




start at Street i "door" [0]
if ^ street i+1 'door' stays  [0]
if > street i+1 stays 'door' [1]

the number in each position increases = its value +1


'''


cols = 150
rows = cols


def Part1(data):
       
    street = 0
    house = 0
    delivered = 0
    ListA = [[0 for _ in range(cols)] for _ in range(rows)]
    ListA[0][0]=1            #Already delivered a present at the first house
    for i in range(len(data)):
        if data[i] == "^":
            street += 1     #If up arrow increase street value
            print('Up Street')
        if data[i] == "v":
            street -= 1     #If down arrow decrease street value
            print('Down Street')
        if data[i] == ">":
            house +=1       #If right arrow increase house value
            print('Right House')
        if data[i] == "<":
            house -=1       #If left arrow decrease house value
            print('left House')


        while len(ListA) <= street:                 #if the required is out of range add "0" to fill the space (missed Streets)
            ListA.append([0] * len(ListA[0]))



        for row in ListA:
            while len(row) <= house:            #if the required is out of range add "0" to fill the space (missed houses)
                row.append(0)


        ListA[street][house] = ListA[street][house]+1  #add a visit to the house, if visited already increase the number of visits

    for i in range(len(ListA)):
        for x in range(len(ListA[i])):
            if ListA[i][x] > 0:
                delivered += 1 


    print(f'Number of Houses delivered to: {delivered}')


def Part2(data):
   
    Santa_street,Santa_house,Robot_street,Robot_house,delivered = 0,0,0,0,-1
    ListA = [[0 for _ in range(cols)] for _ in range(rows)]
    ListA[0][0]=1            #Already delivered a present at the first house

   
    for i in range(len(data)):
        if i%2 !=0:
            if data[i] == "^":
                Santa_street += 1     #If up arrow increase street value
                print('Santa Up Street')
            if data[i] == "v":
                Santa_street -= 1     #If down arrow decrease street value
                print('Santa Down Street')
            if data[i] == ">":
                Santa_house +=1       #If right arrow increase house value
                print('Santa Right House')
            if data[i] == "<":
                Santa_house -=1       #If left arrow decrease house value
                print('Santa left House')
        else:
            if data[i] == "^":
                Robot_street += 1     #If up arrow increase street value
                print('Robot Up Street')
            if data[i] == "v":
                Robot_street -= 1     #If down arrow decrease street value
                print('Robot Down Street')
            if data[i] == ">":
                Robot_house +=1       #If right arrow increase house value
                print('Robot Right House')
            if data[i] == "<":
                Robot_house -=1       #If left arrow decrease house value
                print('Robot left House')



        while len(ListA) <= Santa_street:                 #if the required is out of range add "0" to fill the space (missed Streets)
            ListA.append([0] * len(ListA[0]))

        while len(ListA) <= Robot_street:                 #if the required is out of range add "0" to fill the space (missed Streets)
            ListA.append([0] * len(ListA[0]))



        # for row in ListA:
        #     while len(row) <= Santa_house:            #if the required is out of range add "0" to fill the space (missed houses)
        #         row.append(0)

        # for row in ListA:
        #     while len(row) <= Robot_house:            #if the required is out of range add "0" to fill the space (missed houses)
        #         row.append(0)

        offset = 75
        ListA[Santa_street+offset][Santa_house+offset] = ListA[Santa_street+offset][Santa_house+offset]+1  #add a visit to the house, if visited already increase the number of visits
        ListA[Robot_street+offset][Robot_house+offset] = ListA[Robot_street+offset][Robot_house+offset]+1  #add 500 as an offset, half way down the streets, half way across the houses

    for i in range(len(ListA)):
        for x in range(len(ListA[i])):
            if ListA[i][x] > 0:
                delivered += 1 
    
    # for i in range(len(ListA)):
    #     print(ListA[1])


    print(f'Number of Houses delivered to by Santa and Robot: {delivered}')





