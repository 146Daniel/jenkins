leap_year = int(input("what is the year "))

check = leap_year % 4 

if check == 0: 
    print("the year " + str(leap_year) + " is a leap year." )
else: 
    print("the year " + str(leap_year) + " is not a leap year." )

