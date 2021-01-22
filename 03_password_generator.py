
import random
from datetime import date

today = date.today()
print(today)


def password_gen(length = 6):

    """Generates a password(a string) from a random list of characters"""

    characters = ['a','B','A','c','d', 'D', 'f', 'F', '1', '&',
              '3', 'h', '9', '7', '%', 't', '5', 'y', 'Y', '0',
              '2', '@', 'v', 'r', 'P', ')', '/', 'W', 'Z', '4']
    password = '' 
    for v in range(length):
        character = random.choice(characters)
        password += character 
    print("your password is: ", password)

password_gen(15)

