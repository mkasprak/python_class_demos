test_times = ["Breakfast", "Lunch", "Dinner", "Bedtime"]
sugars = []
for time in test_times:
    level = int(input(f"Enter your blood sugar level for {time}: "))
    sugars.append([time, level])

print(sugars)

print(sugars[0][0], sugars[0][1])
# don't eat too much cheap chocolate!