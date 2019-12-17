# this programme generates two random numbers and tells you to multiply them together
import random

x = int(random.randint(0,10))
y = int(random.randint(0,10))
z = x * y
print("what is; " , x, "*" , y, "?")
a = int(input("Please enter your value:"))

if a == z:
    print('that is the correct answer');
else:
    print('that is not the correct answer')
    print('the correct answer is:', z)




