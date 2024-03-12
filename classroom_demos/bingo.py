# Bingo song in python
def main():
    name_o = "BINGO"
    char_o = list(name_o)
    duck_o = []
    while len(char_o) >= 0:
        print(f"There was a farmer who had a duck and Bingo was his name-o, ")

        for char in char_o:
            print(char, end=" ")
        for quack in duck_o:
            print(quack, end=" ")

        print("\n\n")

        if len(char_o) == 0:
            break
        char_o.pop()
        duck_o.append("👏🐣🐩🐈")


main()
