# not useable

x = input()  # expect a number from the user
y = int(input())  # expect a number from the user, convert it to an integer

print(x * y)

# Better

x = input("Please enter a whole number.  ")  # expect a number from the user
# expect a number from the user, convert it to an integer
y = int(input("Please enter another whole number.  "))

print(x * y)
