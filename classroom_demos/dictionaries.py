def main():
    emoji={"duck":"🐥", "python":"🐍", "monkey":"🙈🙉🙊",
            "dog":"🐶", "cat":"🙀", "fish":"🐠", "bird":"🦜", "bug":"🐞"}
    
    # print(emoji)
    # # accessing an item by its key
    # print(emoji["duck"])
    # animal = emoji.get("cat")
    # print(animal)

    # # get the keys
    # print(emoji.keys())

    # # get the values
    # print('\n\n')
    # print(emoji.values())

    # # get the key value pair
    # print('\n\n')
    # print(emoji.items())

    # if "duck" in emoji:
    #     print(emoji["duck"])

    # emoji["duck"] ="🦆"
    # print(emoji["duck"])

    # emoji.update({"raccoon": "🦝"})

    # removing items
    # emoji.pop("cat")
    # print(emoji)

  
    # del emoji["duck"]
    # print(emoji)

    # print keys
    for x in emoji:
        print(x)

    # print values
    for x in emoji:
        print(emoji[x])

dictionary= {"a":"🍎", " ":" ", "b":"🍌", "q":"👸🏻", ".":"."}

main()