# This is Day 3
import re
import tools as T




with open('data.txt', 'r') as file:
    data = file.read()



# Regular expression to extract `mul({int},{int})`
pattern = re.compile(r"mul\(\d+,\d+\)")
# Extract all matches into a list
results = pattern.findall(data)


def split_and_add_to_lists(data, listA, listB):
    """
    Parses a string like "mul(192,104)" and adds the first and second integers 
    to listA and listB respectively.
    """
    # Regular expression to match the pattern `mul({int},{int})`
    pattern = re.compile(r"^mul\((\d+),(\d+)\)$")
    
    # Match the data against the regex
    match = pattern.match(data.strip())
    if match:
        # Extract the two integers
        int1, int2 = int(match.group(1)), int(match.group(2))
        # Add to respective lists
        listA.append(int1)
        listB.append(int2)




listA = []
listB = []

#Split each num line to 2 lists
for line in range(len(results)):
    split_and_add_to_lists(results[line], listA, listB)

Sum = []

#Run through lists and 
for i in range(len(listA)):
    Sum.append(listA[i] * listB[i])


print(f'{T.CYAN}The Answer for Day 3 is: {T.BLUE} {sum(Sum)}{T.RESET}')


##############################################################
##############################################################
##############################################################
##############################################################


##############################################################
#Create new line each time do or don't appears
#then splint in to list 
##############################################################



split_list = []
DoList = []

##########################################
#Split string, by adding return on every do and dont
#then if "do" add to DoList
#doing on the "ELSE" so it catches the start
##########################################
def add_line_breaks(input_string):
    # Replace "do" and "don't" with a version including a newline
    modified_string = input_string.replace("\n", "").replace("do", "\ndo").replace("don't", "\ndon't")
    split_list = modified_string.split("\n")
    # Remove any empty elements caused by splitting
    split_list = [line for line in split_list if line.strip()]
    for i in range(len(split_list)):
        if split_list[i].startswith("don't()"):
            pass  
        else:    
            DoList.append(split_list[i])
    T.PrintList(DoListOut, T.CYAN, "Do List Out")

    return DoList

DoListOut = DoList
T.PrintList(DoListOut, T.CYAN, "Do List Out")

result = add_line_breaks(data)








DoMulList = []
# Regular expression to extract `mul({int},{int})`
pattern = re.compile(r"mul\(\d+,\d+\)")

# Extract all matches into a list
for i in range(len(result)):
    SumsDo = pattern.findall(result[i])
    DoMulList.append(SumsDo)




TotalMulList = []



for i in range(len(DoMulList)):
    for x in range(len(DoMulList[i])):
        TotalMulList.append(DoMulList[i][x])

DoListA = []
DoListB = []

#Split each num line to 2 lists
for line in range(len(TotalMulList)):
    split_and_add_to_lists(TotalMulList[line], DoListA, DoListB)



Sum = []

#Run through lists and 
for i in range(len(DoListA)):
    Sum.append(DoListA[i] * DoListB[i])


print(f'{T.CYAN}The Answer for Day 3 Do List is: {T.BLUE} {sum(Sum)}{T.RESET}')

#for i in range(len(DoListA)):
#    print(f'({i}) {DoListA[i]} * {DoListB[i]} = {(DoListA[i]*DoListB[i])}')
#    Sum.append(DoListA[i]*DoListB[i])
    



print(sum(Sum))    




print(f'{T.RED}Wrong answers= 83950340,167900680')