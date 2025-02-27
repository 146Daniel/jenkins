
user_input = input("Enter your name: ")
print("Hi " + user_input + "!")

x = input("Enter a number: ")
y = input("Enter another number: ")
print("The sum of the numbers is: ", int(x) + int(y))

x = input("Enter a number: ")
print("The square of the number is: ", int(x) ** 2)

import datetime
current_year = datetime.datetime.now().year
year_of_birth = input("Enter your year of birth: ")
print(f"{user_input} You are", current_year - int(year_of_birth), "years old")



number = input("Enter a three digits number: ")
if len(number) != 3:
    print("The number is not three digits")
else:
    print("your last digit is ", number[-1])
    print("your middle digit is ", number[1])
    print("your first digit is ", number[0])
    avarage =  (int(number[0]) + int(number[1]) + int(number[2])) / 3
    print("The avarage of the digits is: ", "{:.3f}".format(avarage))
