# This is Day 2
import os

from mytools.colors import BLUE


print(BLUE)



with open('data.txt', 'r') as file:
    data = file.read()



DATA_DICT = {}



for index, line in enumerate(data.strip().split("\n")):
    # Creating a list of Integers from the space-separated numbers In the line
    DATA_DICT[index] = list(map(int, line.split()))




SAFE_INC = []
SAFE_INC_3= []

SAFE_DEC = []
SAFE_DEC_3= []
NOT_SAFE = []

SECOND_TRY = []

Y = 0

################################
#'''CHECK IF INCREASING'''
################################
for I in range (len(DATA_DICT)):
    IS_SAFE = True
    for x in range (len(DATA_DICT[I])-1):
        if not (DATA_DICT[I][x] < DATA_DICT[I][x + 1]):
            IS_SAFE = False
            break
    if IS_SAFE:
        SAFE_INC.append(DATA_DICT[I])
    else:
        del DATA_DICT[I][x]
        SECOND_TRY.append(DATA_DICT[I])
################################
#'''CHECK IF INCREASING AND 3 LIMIT'''
################################
for I in range(len(SAFE_INC)):
    IS_SAFE = True
    for x in range (len(SAFE_INC[I])-1):
        if not (SAFE_INC[I][x + 1] - SAFE_INC[I][x] >=1 and SAFE_INC[I][x + 1] - SAFE_INC[I][x] <=3):
            IS_SAFE = False
            break
    if IS_SAFE:
        Y +=1
        SAFE_INC_3.append(SAFE_INC[I])
    else:
        SECOND_TRY.append(SAFE_INC[I])
 

################################
#'''CHECK IF DECREASING'''
################################
for I in range (len(DATA_DICT)):
    IS_SAFE = True
    for x in range (len(DATA_DICT[I])-1):
        if not (DATA_DICT[I][x] > DATA_DICT[I][x + 1]):
            IS_SAFE = False
            
            break
    if IS_SAFE:
        SAFE_DEC.append(DATA_DICT[I])

################################
#'''CHECK IF DECREASING AND 3 LIMIT'''
################################

for I in range(len(SAFE_DEC)):
    IS_SAFE = True
    for x in range (len(SAFE_DEC[I])-1):
        if not (SAFE_DEC[I][x] - SAFE_DEC[I][x + 1] >=1 and SAFE_DEC[I][x] - SAFE_DEC[I][x + 1] <=3):
            IS_SAFE = False
            
            break
    if IS_SAFE:
        Y +=1
        SAFE_DEC_3.append(SAFE_DEC[I])
    else:
        SECOND_TRY.append(SAFE_DEC[I])




INC = len(SAFE_INC_3)
DEC = len(SAFE_DEC_3)
not_safe = len(NOT_SAFE)
print(f'SAFE INCREASE WITH 3: {INC}')
print(f'SAFE DECREASE WITH 3: {DEC}')
print(f'{tools.CYAN}TOTAL SAFE: {INC + DEC} {tools.RESET}')
print(f'TOTAL NOT SAFE: {not_safe}')

print(f'FALSE {len(SECOND_TRY)}')