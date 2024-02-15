# This program manages ticket sales for an event.
print ("\n\n")

# Initialize seating list
seats = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

print ("Current available seats: ")
print (seats) # Show available seating to customer
print ("\n")

# Until customer enters 0 we sell tickets

choice = 1

while choice != 0:
    choice = input ("Please select seats to purchase, enter '0' when finished: ")

    if choice in seats:
        seats.remove(choice)
        print ("Current available seats:")
        print (seats)
        print ("\n")
    elif choice == '0':
        break
    else:
        print ("Something went wrong. Please try again")
    
    
# Goodbye
print ("\nThanks for your purchase~!\n")