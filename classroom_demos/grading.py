# This program validates passwords.
print("\n\n")


def validate_password_length(string): # Checks if string is the right length.
    if len(string) < 8 or len(string) > 20:
        print ("\nPassword must be between 8 and 20 characters long.")
        return False
    else:
        return True
          
def validate_password_lowercase(string): #Counts lowercase characters to know if there's at least one.
    lower_counter = 0

    for ch in string:
        if ch.islower():
            lower_counter += 1
        

    if lower_counter < 1:
        print ("Please use at least one lowercase character.")
        return False
    else:
        return True
    

def validate_password_uppercase(string):  #Counts uppercase characters to know if there's at least one.
    upper_counter = 0

    for ch in string:
        if ch.isupper():
            upper_counter += 1

    
    if upper_counter < 1:
        print ("Please use at least one uppercase character.")
        return False
    else:
        return True
        
def validate_password_num(string):  # Counts numeric characters to know if there's at least one.
    number_counter = 0

    for ch in string:
        if ch.isnumeric():
            number_counter += 1
            return True
    
    if number_counter < 1:
        print ("Please use at least one number.")
        return False


def validate_password_symbol(string): # Checks if there's one of the list symbols in the password.
    symbol_list = ["!", "@", "#", "$", "%", "&", "*"]
    is_symbol = False

    for ch in string:
        if ch in symbol_list:
            is_symbol = True
            return True

    if not is_symbol:
        print ("Please use one of these symbols: ! @ # $ % & *")
        return False


def main():
        password_invalid = True
        while password_invalid:
            try:
                print("""\nPassword Requirements:\n
                    Between 8 to 20 characters long.\n
                    Contains at least one uppercase letter.\n
                    Contains at least one lowercase letter.\n
                    Includes at least one number.\n
                    Includes at least one symbol from the set: !@#$%&*\n""")
                    
                password = input("Please enter a password that meets the criteria: ")

                # Call all functions to validate and store the boolean returned
                is_length = validate_password_length(password)
                is_lowercase = validate_password_lowercase(password)
                is_uppercase = validate_password_uppercase(password)
                is_num = validate_password_num(password)
                is_symbol = validate_password_symbol(password)

                # If all booleans are true we break the loop and continue to password confirmation
                if is_length and is_lowercase and is_uppercase and is_num and is_symbol:
                    password_invalid = False
                    password_confirmation = input("Please re-type the password for confirmation: ")

                    while password != password_confirmation:
                        print ("Hmm. That's not a match. Try again.")
                        password_confirmation = input("Please re-type the password for confirmation: ")
                    else:
                        print ("Congratulations! You made a password.")
                else:
                    continue

            except:
                print ("Something went wrong!")






main()