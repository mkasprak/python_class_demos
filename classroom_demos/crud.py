'''
    CRUD practice

'''
def check():
    try:
        file = open("customer_list.txt", 'r')# does the fle exist?
        lines = file.readlines()
        # for line in lines:
        #     print(line) This was for test purposes!
        file.close()
        return lines
    except:
        lines = []
        print("Customer list does not exist. I will create a new file ")
        return lines

def create():
    try:
        customer = check()
        fname = input("Please enter the customer\'s first name:  ")
        lname = input("Please enter the customers\'s last name:  ")
        phone = input("Please enter the customer's phone:  ")
        email = input("Please enter the customer's email:  ")
        entry = (fname + ", " + lname + ", " + phone + ", "  + email + "\n")
        customer.append(entry)
        save(customer)
    except Exception as e:
        print(e)
    
    main()

def read():
    output = search()
    print(output)
    main()

def update():
    try:
        output, index_nbr= search()
        entry = output.split(", ")
        lname = entry[0]
        fname = entry[1]
        phone = entry[2]
        email = entry[3]
        print("1: " + lname + "\n2: " + fname + "\n3: " + phone + "\n4: " + email )
        choice  = int(input("Enter the number of the value that you want to change: "))
        if choice == 0:
            lname = input("Please enter the new last name: ")
        elif choice == 1:
            fname = input("Please enter the new first name: ")
        elif choice == 2: 
            phone = input("Please enter a new phone number: ")
        elif choice == 3: 
            email = input("please enter a new email:  ")
    
        # delete old record
        customer = check()
        del customer[index_nbr]

        # add new record
        entry = (fname + ", " + lname + ", " + phone + ", "  + email + "\n")
        customer.append(entry)
        save(customer)
    
    except Exception as e:
        print(f"Update problem! {e}")

    main()

def delete():
    try:
        customer = check()
        print("We will search for the entry you want to delete. ")
        output, index_nbr= search()
        print(output)
        confirm = input("Do you want to delete this record? (y/n)  ")
        if confirm.lower() == 'y':
            print("deleting")
            del customer[index_nbr]
        else:
            print("We will not delete. ")
    except Exception as e:
        print(f"Error deleting: {e}")
    
    main()

def search():
    # So I can find what I am looking for!
    try:
        lname = input("Please enter the last name of the person you want to look for:  ")
        customer = check()
        found = ''
        for c in customer:
            if lname.upper() in c.upper():
                found = c
                index_nbr = customer.index(c)
                return found, index_nbr
    except Exception as e:
        print(f"Read error! : {e}")
    main()

def save(output):
    print("Saving")
    for line in output:
        print(line) 
    try:
        file = open("customer_list.txt", 'w')
        for line in output:
            file.write(line)
        file.close()
        print("File updated.")
    except Exception as e:
        print(f"Save did not work. \n {e}")



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
    except Exception as e:
        print(e)
        
main()