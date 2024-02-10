'''
    Demonstration of the Bubble Sort algorithm.
'''

numbers = [8, 6, 7, 6, 5, 3, 0, 9]
swapped = True  # Flag - we are priming this to make sure it runs at least once

while swapped:
    swapped = False  # resetting the flag
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            swapped = True  # a swap occurred!
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

print(numbers)

names = ["Bob", "Carol", "Ted", "Alice", "Anna"]
swapped = True  # Flag - we are priming this to make sure it runs at least once
while swapped:
    swapped = False  # resetting the flag
    for i in range(len(names) - 1):
        if names[i] > names[i + 1]:
            swapped = True  # a swap occurred!
            names[i], names[i + 1] = names[i + 1], names[i]

print(names)
names.reverse()
print(names)
