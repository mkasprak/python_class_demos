
# creating and using tuples

def main():
    months = ("January", "February", "March", "April", "May", "June", "July", "August", 
              "September", "October", "November", "December")
    
    for month in months:
        print(month, end = "  ")
    
    print(f"\nThere are :  {len(months)} months in  a year")
    summer = []
    summer.append(months[4:7])
    print("Summer includes: ")
    for month in summer:
        print(month, end= "  ")
    print("\n\n")
    summer.append("August")
    print(summer)


main()