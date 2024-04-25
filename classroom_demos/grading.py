

#Creating a main function so i can call it later 
def main(): 
    #making a list for all the information that I need 
    nato_alphabet = {"A":"Alpha", "B":"Bravo", "C":"Charlie", "D":"Delta", "E":"Echo", "F":"Foxtrot", "G":"Golf", "H":"Hotel", "I":"India", "J":"Juliette", "K":"Kilo", "L":"Lima", 
                     "M":"Mike", "N":"November", "O":"Oscar", "P":"Papa", "Q":"Quebec", "R":"Romeo", "S":"Sierra","T":"Tango","U":"Uniform","V":"Victor","W":"Whiskey",
                     "X":"X-Ray","Y":"Yankee","Z":"Zulu"}
    #Printing out the names so the user can pick one from this list
    print(nato_alphabet)
    #Asking the user to type a name form one that is inside the list 
    quest = input("Enter a word from the the nato alphabet list please: ")

    for i in quest: 
        print(quest)
#Calling the list so it can work 
main()