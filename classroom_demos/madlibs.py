def main():
    words = get_words()
    print(words)
    madlibs() 


def get_words():
    person = input("Please enter a name:  ")
    animal = input("Please enter a kind of animal:  ")
    return person, animal

def madlibs():
    print("I'm in Madlibs!")


main()