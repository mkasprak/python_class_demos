#other functions would come at the top

# globals
g_bunny = "Giant chocolate bunny"



def get_list(name):
    print(name)
    flag = True
    easter_basket = []
    print(f"Hi! {name}!")
    print("Please enter 'full' when you are done. ")
    while flag:
        candy = input("What kind of candy or toy do you want for easter:  ")
        if candy == 'full':
            break
        easter_basket.append(candy)
    basket = input("What kind of basket do you want? (plastic, wood, et.):  ")
    return easter_basket, basket


def main():
    
    my_name = input ("Hi! Who are you?  ")
    my_list, basket = get_list(my_name)
    print(my_list)
    print(basket)
    
    

main()

