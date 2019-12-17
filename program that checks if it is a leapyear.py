# Program that finds leap year

year1 = int(input("please enter the year to check if it is a leap year or not:"))
leapyear = year1 % 4
if leapyear == 0:
    print("it is a leapyear")
else:
    print("it is not a leapyear")
    
