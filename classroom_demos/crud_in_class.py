"""
    CRUD application for creating an address book.
    This will have some problems in it. you may solve the problems 
    for extra credit:
    Does not allow for duplicate names to be properly handled
    Search searches the entire entry not a specific field


    🚨 Avoid project creep!


"""


def main_menu():
    # present menu
    # Check values 
    # return choice
    try:
        print("\nMain Menu - Customer Directory")
        print("1. Create new entry")
        print("2. Read and display by name")
        print("3. Update a record")
        print("4. Delete a record")
        print("5. Quit")
        choice = int(input("Please enter the number of your selection: "))
        if choice < 0 or choice > 5:
            print("That is out of range, please try again.")
            main_menu()
        else:
            return choice
    except ValueError:
        print("That is not a valid number. Please try again.")
        main_menu()
    except Exception as e:
        print(f"main_menu: {e}")

def check():
    # read file to list
    # if file not there create empty customer list
    # return customer list
    try:
        file = open("customer_directory.txt", "r")
        curr_customer = file.readlines()
        for line in curr_customer:
            print(line) # This was for test purposes!
        file.close()
        return curr_customer
    except FileNotFoundError:
        print("That file does not exist. \n We will create a new file for you!")
        curr_customer = []
        return curr_customer
    except Exception as e:
        print(f"Check: {e}")
    
# save need the parameter of current Users (str Array)
# array will be saved to the file, file will override all customers in customer, to re save ALL 
# Array = list, collection of the users in a list 
# open file in write mode, write then close 
def save(curr_customer): #save will save the CURR_CUSTOMER from param
    # save the file

    #Save does not need to preform advanced CHECK before saving, as check should *ALWAYS*
    # be called before using CHECK, otherwise issues 
    # check before create, update, and all remaining crud operations

    #open file to save 
    try:
                                    # open in w WRITE mode, for saving to file 
        to_save_file = open("customer_directory.txt", "w")

        # LOOP through list of customers, and write them to the .txt

        for record in curr_customer: 
            print("Saved line to record: ", record)
            #use to save and save the record to the file 
            to_save_file.write(record)
        # all customers written to file 
        print("finnished saving customers", curr_customer)


        to_save_file.close()

        
    except IOError:
        print("SAVE: Error occured during save file operation, IOError")
        



    print("Save")
    main()

def create():
    # create a new entry
    # call the save  function
    try:
        customers = check()
        print("\n Please enter the customer information: ")
        first_name = input("First name: ")
        last_name = input("Last Name: ")
        phone = input("Phone number: ")
        email = input("Email address: ")
        entry = f"{first_name}, {last_name}, {phone}, {email}\n"
        #Fix: BUG-FIX: Brackets were converting data to set, removed, 
        #DATA SHOULD BE SENT IN LIKE A ARRAY, *BUT* formated as STRING, 
        #so it looks like array
        customers.append(entry)

        #Debug loop 
        for line in customers:
            print(line)
        
        #AFTER Debug loop, 
        #Implment save customers 
        save(customers)

    except Exception as e:
        print(f"Create: {e}")
    main()

def read():
    # will call the search function
    # will display the found record, (also print index cause its given on return)
    print("read")

    #Call search function to search 

    #run in try-except
    try: 
        
        #call SEARCH
        found_customer, found_index = search()

        print(f"System Found Customer: {found_customer} at index: {found_index}😁")

    except Exception as e:
        print(f"READ: {e}")

    main()

def search():
    # called by - read, update, delete
    # returns - record, index

    #TRY checking for customer entries and retrieve all entered customers 
    try:
        #Call check function 
        curr_customers = check()

        
        record_to_search = input("Enter a name or part of a name to find a specific customer: ")

        # iterate throgh the customers and check 
        #EACH entry, 
        #IF cust contains EXSISTING CUSTOMER, then exists, 
        #if not, not exist :(
        for cust in curr_customers:
            #looping through customers 
            print(f"searching customers: {cust}")
            #Check if record to search is the customer being current searched 
            if record_to_search in cust:
                print("FOUND\n")
                #CUSTOMER EXISTS:
                
                #break out index from customer (confirmed to exists at this point)
                customer_index = curr_customers.index(cust)
                
                #Return both searched RECORD, and index 

                return cust, customer_index

            else:
                #CUSTOMER DOES NOT EXISTS HERE
                print("CUSTOMER DOES NOT EXISTS, Please try searching again 😩\n")

            





    except Exception as e:
        print(f"Search: {e}")


    print("Search")

def update():
    # updates a record
    # uses search function
    print("Update")
    main()

def delete():
    # calls search
    # verifies that it is the record to delete
    # deletes the record
    print("delete")
    main()



def main():
    choice = main_menu()
    try:
        if choice == 1:
            create()
        elif choice == 2:
            read()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
        else:
            print("Goodbye!\n")
    except Exception as e:
        print(f"Main: {e}")

main()