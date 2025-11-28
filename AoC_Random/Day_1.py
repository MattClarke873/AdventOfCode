'''
🐍 Daily Python Challenge – Day 1

Title: Sum of Digits

Task:
Write a Python function sum_of_digits(n) that takes an integer n and returns the sum of its digits.

Examples:

sum_of_digits(123)   # 6
sum_of_digits(9875)  # 29
sum_of_digits(0)     # 0


Extra Challenge (Optional):
Keep summing the digits until the result is a single digit.
For example:

9875 → 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = 2

Final answer = 2.'''



'''
Title: Sum of Digits

Task:
Write a Python function sum_of_digits(n) that takes an integer n and returns the sum of its digits.

sum_of_digits(123)   # 6
sum_of_digits(9875)  # 29
sum_of_digits(0)     # 0

'''

def sum_of_digits(n):
    while n >= 10:  # keep looping until single digit
        total = 0
        for digit in str(n):
            total += int(digit)
        n = total
    return n




def digital_root_math(n):
    return 0 if n == 0 else 9 if n % 9 == 0 else n % 9

	
	
print(sum_of_digits(9875))

print(digital_root_math(9875))