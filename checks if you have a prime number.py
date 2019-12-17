#This programme checks if the number you have inputted is a prime number or not
loop = 1 == 1
while loop == True:

    for num in range(1,100):
        number = int(input("Enter a number:"))
    if all(number%i!=0 for i in range(2,num)):
        print("this is a prime number")
