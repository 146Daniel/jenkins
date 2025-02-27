import random
import string

def get_random_string(length):

    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Your random password of", length, "characters is:", result_str)
user_choise = int(input("Enter the length of the password you want to generate: "))
get_random_string(user_choise)