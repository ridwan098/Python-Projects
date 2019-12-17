# Program to check if you have entered the right password

import str
from random import *

letters = str.ascii_letters
digits = str.digits
symbols = str.puntuation
chars = letters + digits + symbols

min_length = 8
max_length = 16
password = "".join(choice(chars)for x in range(random.randint(min_length, max_length)))
print(password)

randint
