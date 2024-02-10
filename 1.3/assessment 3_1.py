# Initialize lists
scores = []
letter_grades = []

# Collect and process 10 grades
print("You are going to enter ten assignment scores. Each score should be between 0 and 100.")
print("I will calculate the average and assign a letter grade.")
for i in range(10):
    grade = float(input("Enter grade: "))
    scores.append(grade)

    # Determine letter grade
    if grade >= 90:
        letter_grades.append('A')
    elif grade >= 80:
        letter_grades.append('B')
    elif grade >= 70:
        letter_grades.append('C')
    elif grade >= 60:
        letter_grades.append('D')
    else:
        letter_grades.append('F')

# Display letter grades
print("\nLetter Grades:")
for y in range(10):
    print("Assignment " + str(y+1) + ": " + "Score of " +
          str(scores[y]) + " Letter Grade: " + letter_grades[y])

# Calculate and display average
average = sum(scores) / len(scores)
print(f"\nAverage Score: {average}")

# Determine and display letter grade for average
if average >= 90:
    print("Average Letter Grade: A")
elif average >= 80:
    print("Average Letter Grade: B")
elif average >= 70:
    print("Average Letter Grade: C")
elif average >= 60:
    print("Average Letter Grade: D")
else:
    print("Average Letter Grade: F")
