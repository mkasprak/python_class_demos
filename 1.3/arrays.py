'''
    Demonstration of  arrays in python for storing blood sugar levels
'''

# create an array of  test times
test_times = ["Breakfast", "Lunch", "Dinner", "Bedtime"]
sugars = []


for time in test_times:
    level = int(input(f"Enter your blood sugar level for {time}: "))
    sugars.append([time, level])

print(sugars)

# print the array

# calculate the average blood sugar level
total = 0
for sugar in sugars:
    total += sugar[1]

average = round(total / len(sugars))
print("Your average blood sugar level is ", average)
