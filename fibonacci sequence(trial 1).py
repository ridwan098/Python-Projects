
# This program prints out the fibonacci sequence(up to 100)
loop = 1 == 1
while loop == True:

    number = 1
    last = 0
    before_last = 0


    num = int(input("\nHow many times should it list? "))
    for counter in range(0, num):
        before_last = last
        last = number
        number = before_last + last
        print(number)
