"""
    Creating and using a Dog SuperClass 🐕
    and a herding dog sub class 🐏🐏🐏

    and instantiating (making objects)
"""


class Dog:
    # dog is a Super class of the Herding_Dog class
    def __init__(self, color, coat, size, name):
        self.color = color
        self.coat = coat
        self.size = size
        self.name = name

    def bark(self):
        print("Woof!")

    def happy(self):
        print("Wag wag")

    def __str__(self):
        return f"Dog: Color: {self.color}, Coat: {self.coat}, Size: {self.size}, Name:{self.name}"


class HerdingDog(Dog):
    def herding(self):
        print("Go over here! Get me a cookie!")

    def __str__(self):
        return super().__str__() + ", with herding skills"


def main():

    print("\n\n")
    ollie = Dog("Fawn", "Short", "Large", "Ollie")
    print("Ollie: ")
    ollie.bark()
    ollie.happy()
    print(ollie)

    print("\n\n")
    print("Nessie:")
    nessie = HerdingDog("Black", "Short", "Large", "Nessie")
    nessie.herding()
    print(nessie.__str__())
    print("\n\n")


main()
