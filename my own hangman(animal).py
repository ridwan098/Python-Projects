# This is a Hangman game- my orginal idea is to choose from different topics that you want
import random

#1)
name = input('Welcome! What is your name?\n')
print('Hello,',name,'Lets play Hangmam!')

#2)Categories
Animal = ['bird', 'dog', 'cat', 'deer', 'bear', 'reptile', 'gray wolf', 'snake', 'raccoon', 'squirrel', 'horse', 'lion', 'mouse', 'bat', 'turtle', 'crocodile', 'leopard']
Countries = ['china', 'india', 'united states', 'indonesia', 'brazil', 'pakistan', 'nigeria', 'bangladesh', 'russia', 'japan', 'mexico', 'ethiopia', 'vietnam', 'egypt', 'iran', 'congo', 'germany', 'france', 'south africa', 'united kingdom', 'italy']
Planets = ['' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '']

#3)



#4)
print('\nDo you know the categories?')
quest1 = input()


if quest1 == 'no' or 'No':
    print('The categories to the game are: Animals, Countries and Planets')
    print('Choose a category from the list:')
    category = input()

if quest1 == 'yes' or 'Yes':
    print('Choose a category from the list:')
    category = input()

#6) player picks category and  then starts guessing
if category == 'Animal' or 'animal':
    chosenword = random.choice(Animal)

    turns = 11
    while turns > 0:
        failed = 0
    print('Start guessing...')

    
#**question** how do you limit this to one letter?
    guess = input('guess a character: ')

#7)checks each letter guessed
    for i in guess:
        
        if i in chosenword:
            print(guess)

        if guess not in chosenword:
            print('_',)
            failed += 1
    
#8)
    if failed == 0:
        print('Congratulations!',name,'You won')
        #break

    print('')
    
    
#10)
    if guess not in chosenword:
        turns -= 1
        print('Wrong')
        print('You have',turns,'more guesses left',name)

        if turns == 0:
            print('You Loose, \n The answer was', chosenword, '\nstart again (by pressing F5)')
