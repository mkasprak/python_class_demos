# Start with a try
def main():
    try:
        print(10/2)
        my_list=(1,2,3,4)
        print(my_list[2])
    
    except IndexError:
        print("Out of range! 🏔️")
    except ZeroDivisionError:
        print("You are not allowed to divide by 0 😭")
    except:
        print("That won't work! 👎🏽")

    else:
        print("Division successful!")
    finally:
        print("Execution completed.")





main()