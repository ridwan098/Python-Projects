import random

loop = 1 == 1
while loop == True:

    a = input('is your number international?:')
    

    if a == 'yes' or a == 'Yes':
      number12 =  input('what is your country code?:\n')
      number22 = random.randint(1000, 9000)
      number33 = random.randint(1000, 9000)
      phoneNum1 = number12, number22, number33
      print("your random number is:",phoneNum1)
      
      print();


    else:
        print('your number is not international so...')
        number1 = input('what number does it start with?:\n')
        number2 = random.randint(1000, 9000)
        number3 = random.randint(1000, 9000)
        phoneNum = number1, number2, number3
        print("your random number is:",phoneNum)
        print()
    

                
