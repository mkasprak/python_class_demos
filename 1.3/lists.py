'''
1. create a list with the days of the week
2. create an empty list called steps
3. Use your days list to ask the user how many steps they took on each day of the week
4. Append the user's input to the steps list
5. Display the steps for each day
6. Display the total steps
6. Create a variable called average and calculate the average steps (use the round function)
    average = round(total / len(steps))
7. Display the average steps
'''

days = ["Sunday", "Monday", "Tuesday",
        "Wednesday", "Thursday", "Friday", "Saturday"]
steps = []
for day in days:
    steps.append(int(input("How many steps did you take on " + day + "? ")))
step = 0
print("\n\n")
for day in days:
    print("You took", steps[step], "steps on", day)
    step += 1

print("\n\n")
# Display the total steps
total = 0
for step in steps:
    total += step
print("Total steps: ", total)

# Display the average steps
average = round(total / len(steps))
print("Average steps: ", average)
