# calculate a person's age in: Years, months, weeks, days

from datetime import datetime

def main():
    print("\n\n")
    # now = datetime.now()
    # print(f"now: {now}")
    # timestamp = datetime.now().time()
    # print(f"timestamp: {timestamp}")
    print("\n\n")
    try:
        today = datetime.today()
        print(today.weekday())
        birth_year = int(input("What year were you born?  "))
        month = int(input("What Month were you born (as a number. May would be 5)  "))
        day = int(input("What day of the month were you born?  "))
        # just need datetime not datetime.date
        # because we imported datetime from datetime
        birthday = datetime(birth_year, month, day)
        birth_year = str(birth_year + 10)
       
        print("Your birthday is: ")
        birthday_output = birthday.strftime("%Y-%m-%d")
        print(birthday_output) 
        birthday = birthday.replace(year = 1981)
        print (f"Gee, you look like you were born {birthday}")
        date_string = str(birth_year) + "-" + str(month) + "-" + str(day) 
        dt = datetime.strptime(date_string, "%Y-%m-%d")
        print(dt)
      
    except Exception as e:
        print(f"ooooops!!!:  {e}") 
        main()
main()
