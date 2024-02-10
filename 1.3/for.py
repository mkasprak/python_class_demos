# three arguments
for i in range(1, 10, 2):
    print(i)

# two arguments
for i in range(5, 8):
    print(i)

# break
for i in range(1, 10):
    if i == 5:
        break
    print(i)


# Continue
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)


# Else
for i in range(5):
    if i == 3:
        break
else:
    print("Loop completed without break")
