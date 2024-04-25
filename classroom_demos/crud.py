'''
    CRUD practice

'''
def check():
    print("Check for file")
    # does the fle exist?
    # create empty list if it does not exist
    # read into list if it does exist
    # close file
    # return list

def create():
    print("Create")
    # call check, save list
    main()

def read():
    print("Read")
    main()

def update():
    print("Update")
    main()

def delete():
    print("Delete")
    main()

def save(output):
    print("Save")


def main():
    # present menu and call appropriate functions
    print("\nWelcome! You can create new email entries")
    print("Change email address, delete entries, or display")
    print("\n")
    print("1. Create a new entry")
    print("2. Display an entry by last name")
    print("3. Update an existing entry.")
    print("4. Remove an entry.")
    print("5. Quit")
    
    try:
        choice = int(input("Please enter the number of your selection:  "))
        if choice < 1 or choice > 5:
            print("That is not a valid choice.")
            main()
        if choice == 1:
            create()
        elif choice == 2:
            read()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
        else:
            print("Goodbye!")
    except:
        print("That is not a valid choice, let's start over.")
main()