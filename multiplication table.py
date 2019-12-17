# This program displays the multiplication table
loop = 1 == 1
while loop == True:
    n= input('\nenter an integer:')
    for i in range(1, 13):         
        print ("%s x %s = %s" %(n, i, i*int(n)))
        
