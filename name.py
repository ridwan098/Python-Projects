#this program says hello and asks for your details
import time, sys
print("welcome")
print("what is your name?")
myname=input()
print("it is good to meet you,"+myname)
print("how old are you?")
age=input("write your age here: ")
print("so you are: " +age,"years old")
print ("what school do you go to?")
school=input()

print("are you sure you go to " +school,'?')
answer= input()
if answer == 'yes':
    print("thats good, have a good christmas")  
if answer == 'no':
    print('what school do you go then?')
    school=input()
print("are you sure you go to " +school,'?')
answer= input()
if answer == 'yes':
    print("thats good, have a good christmas")
if answer == 'no':
        print('that was you last chance, i will shut down in three seconds?')
        time.sleep(3)

        #always remember to put 'sfbhfs' in the if statement if that is the response
        #you are looking for.
        
