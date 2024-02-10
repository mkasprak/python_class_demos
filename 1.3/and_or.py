'''
User Input: Prompt the user to enter two integers.
Demonstrate the use of and/or/not statements (2 of each) with the integers. Display the comparison and the result on the screen.
'''

# Prompt the user to enter two integers.
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

# Demonstrate the use of and/or/not statements (2 of each) with the integers. Display the comparison and the result on the screen.

# and
print("Both numbers greater than 0:  ", num1 > 0 and num2 > 0)
print("Both numbers greater than 100: ", num1 > 100 and num2 > 100)

# or
print("Either number is even? ", num1 % 2 == 0 or num2 % 2 == 0)
print("Either number is less than 100?  ", num1 < 100 or num2 < 100)

# not

print("num1 is not equal to num2: ", num1 != num2)
print("num1 is not 0: ", num1 != 0)
