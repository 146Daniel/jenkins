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
