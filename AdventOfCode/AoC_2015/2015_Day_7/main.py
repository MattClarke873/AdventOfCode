''' This is Day *** '''
import time 
import pprint as p

YEAR = 2015
DAY = 7

with open(f'/Users/MattClarke/repo/Advent of Code/AoC/AdventOfCode/AdventOfCode/AoC_2015/2015_Day_7/data.txt', 'r', encoding="utf-8") as file:
    data = file.read().strip()  # read file, and strip -- remove any white space

with open(f'/Users/MattClarke/repo/Advent of Code/AoC/AdventOfCode/AdventOfCode/AoC_2015/2015_Day_7/test_data.txt', 'r', encoding="utf-8") as file:
    test_data = file.read().strip()  # read file, and strip -- remove any white space    




table = {}



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



    """
    Parse the input data into actionable instructions.
    
    Args:
        data: The raw input data as a string.
    
    Returns:
        A list of instructions
    """
    
lines = data.splitlines()
for line in lines:
    l, r = line.split(" -> ")
    table[r] = l
        

mem = {}
 
def get_val(var):
    """
    Function to calculate the value of a given wire or variable using bitwise operations,
    recursively resolving dependencies in the circuit.

    Args:
        var: The variable or wire whose value needs to be calculated.

    Returns:
        The resolved integer value of the variable or wire.
    """

    # Check if `var` is a digit (numeric string), meaning it's a direct value.
    if var.isdigit():
        return int(var)  # Convert it directly to an integer and return it.

    # Check if `var` has already been computed and cached in `mem` (memoization).
    if var in mem:
        return mem[var]  # Return the cached value.

    # Retrieve the instruction for the given `var` from the `table` dictionary.
    s = table[var]
    #print(var, s)  # Debugging statement to show the current variable and its corresponding instruction.

    # If the instruction itself is a direct digit, cache and return it.
    if s.isdigit():
        mem[var] = int(s)  # Store the value in the `mem` cache.
        return mem[var]  # Return the cached value.

    # If the instruction starts with "NOT", it's a bitwise NOT operation.
    if s.startswith("NOT"):
        s1 = get_val(s[4:])  # Recursively resolve the operand after "NOT".
        mem[var] = ~s1 & 0xFFFF  # Perform the 16-bit bitwise NOT and cache the result.
        return mem[var]  # Return the cached value.

    # If the instruction contains "OR", it's a bitwise OR operation.
    if "OR" in s:
        a, b = s.split(" OR ")  # Split the instruction into its two operands.
        mem[var] = get_val(a) | get_val(b)  # Recursively resolve both operands and perform bitwise OR.
        return mem[var]  # Return the cached value.

    # If the instruction contains "AND", it's a bitwise AND operation.
    if "AND" in s:
        a, b = s.split(" AND ")  # Split the instruction into its two operands.
        mem[var] = get_val(a) & get_val(b)  # Recursively resolve both operands and perform bitwise AND.
        return mem[var]  # Return the cached value.

    # If the instruction contains "LSHIFT", it's a left shift operation.
    if "LSHIFT" in s:
        a, b = s.split(" LSHIFT ")  # Split the instruction into the value and shift amount.
        mem[var] = get_val(a) << int(b)  # Resolve the value and perform a left shift by the given amount.
        return mem[var]  # Return the cached value.

    # If the instruction contains "RSHIFT", it's a right shift operation.
    if "RSHIFT" in s:
        a, b = s.split(" RSHIFT ")  # Split the instruction into the value and shift amount.
        mem[var] = get_val(a) >> int(b)  # Resolve the value and perform a right shift by the given amount.
        return mem[var]  # Return the cached value.

    # If no specific operation is found, treat the instruction as a reference to another variable.
    mem[var] = get_val(s)  # Recursively resolve the value for the instruction and cache it.
    return mem[var]  # Return the cached value.




def part1(data):
    """--- Day 7: Some Assembly Required ---
This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?"""
    
    print(get_val("a"))


# x = 123
# y = 456

# print(f'{y} and {x} = d =  {x & y}')
# print(f'{y} or {x} = e = {x | y}')
# print(f'{x} LSHIFT2 = f ={x << 2}')
# print(f'{y} LSHIFT2 = g = {y >> 2}')
# print(f'NOT {x} = h = {~x & 0xFFFF }')
# print(f'NOT {y} = i = {~y & 0xFFFF}')
    



def part2(data):
    """Part 2 is not yet implemented."""
    table['b'] = "3176"
    global mem
    mem = {}
    
    print(get_val("a"))

if __name__ == "__main__":
    # Execute both parts
    answer1 = time_it(part1, data)
    answer2 = time_it(part2, data)




