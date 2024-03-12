import random

"""
    Working with modules, random and math
"""

def main():
    # test random
    guess = 42
    win = random.randint(1,100)
    print(win)
    distance = win - 42
    distance = abs(win)
    if distance <= 42:
        print("hot")
    else:
        print("not")



main()