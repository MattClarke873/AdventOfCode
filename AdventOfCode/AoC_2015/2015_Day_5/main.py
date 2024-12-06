''' This is Day 5 '''


YEAR = 2015
DAY = 5
with open(f'AoC/AdventOfCode/AdventOfCode/AoC_{YEAR}/{YEAR}_Day_{DAY}/data.txt', 'r', encoding="utf-8") as file:
    data = file.read().strip()  # read file, and strip -- remove any white space

with open(f'AoC/AdventOfCode/AdventOfCode/AoC_{YEAR}/{YEAR}_Day_{DAY}/test_data.txt', 'r', encoding="utf-8") as file:
    test_data = file.read().strip()  # read file, and strip -- remove any white space    


def part1(data):
    """Function Solves problem one."""
    nice = 0
    word_list = data.splitlines()

    for word in word_list:
        contains_forbidden = False
        has_double = False
        vowels = 0


        if any(forbidden in word for forbidden in ["ab", "cd", "pq", "xy"]):
            contains_forbidden = True


        for letters in word:
            if letters in "aeiou":
                vowels += 1


        for i in range(len(word) -1):
            if word[i] == word[i + 1]:
                has_double = True
                break


        #Determine if the string is "nice" and all functions are met
        if vowels >= 3 and has_double and not contains_forbidden:
            nice += 1

    print(f"Number of nice strings: {nice}")

def part2(data):
    """Function Solves problem two."""
    nice = 0
    word_list = data.splitlines()
    print('start')
    for word in word_list:
        double_double = False
        repeat = False

        for i in range(len(word) - 1):
            double = None
            if i > 0:
                if word[i-1] == word[i]:
                    double = word[i-1] + word[i]
                    print(f'double {double}')
                for x in range(len(word)-2):
                    if x > 1:
                        double_check = word[x-2] + word[x-1]
                        
                        if double == double_check:
                            print({x-2}, {i-1})
                            if ((x-2) - (i-1))  > 2:
                                print('SNAP')
                                double_double = True
                                break

                            '''NEED TO LOOK IN TO WHY THIS ISNT WORKING?? AAA CANT OVER'''

     

        for i in range(len(word) -1):
            if i > 0:
                sample = word[i-1] + word[i]
                for x in range(len(word) -2):
                    if x > 3:
                        check = word[x-2] + word[x-1] 
                        if check == sample:
                            if not (i-1) == (x-2) and not (i) == (x-1):
                                
                               # print(f'sample letters {sample} check letter {check}')
                               # print(f'sample index {i-1}, {i} check letter index {x-2}, {x-1}')
                                repeat = True
                           

        if double_double and repeat:
            nice +=1


    print(nice)



part2(test_data) 