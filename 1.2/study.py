# Asking user their age
age = float(input("Enter age here: "))

# display if user can drive
if age >= 16:
    print("You are old enough to drive")
else:
    print("You are not old enough to drive")
# display if user can vote
if age >= 18:
    print("You are old enough to vote")
else:
    print("you are not old enough to vote")
# diplay is user can legally buy alcohol
if age >= 21:
    print("you are old enough to buy alcohol")
else:
    print("you are not old enough to buy alcohol")
# display if user is elgible for senior discount
if age >= 65:
    print("you are old enough for senior discount")
else:
    print("you are not old enough for senior discount")
