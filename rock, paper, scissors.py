# this game is a rock paper scissors game

print("welcome to 'rock, paper, scissors' ")
print()
print()
print()
name = input ("Choose between Rock, Paper, Scissors?: \n")
print()
print()

import time
time.sleep(0.2)
x = ('Rock', 'Paper', 'Scissors')


import random
index = random.choice (x)


print("The computer has chosen", index, "!")


if name == 'Rock' or name == "rock":
    if index == "Rock":
        print("you tied the computer, try again!");


if name == "Rock" or name == "rock":
    if index == 'paper':
        print ("You lose, try again");


if name == "Rock' or name == 'rock":
    if index == 'Scissors':
        print('Congratulation, you are the winner');

if name == 'Paper' or name == 'paper':
    if index == 'Rock':
        print('Congratulations, you are the winner !');

if name == 'Paper' or name == 'paper':
    if index == 'Paper':
        print('You have tied with the computer, try again')


if name == 'Paper' or name == 'paper':
    if index == 'Scissors':
        print("You lose, Try again!")

if name == 'Scissors' or name == 'scissors':
    if index == 'Scissors':
        print('You tied the computer, Try again!')


if name == 'Scissors' or name == 'scissors':
    if index == 'Paper':
        print('Congratulation, you have won!')

if name == 'Scissors' or name == 'scissors':
    if index == 'Rock':
        print('You lose, Try again')

import time
time.sleep(3)


import sys
sys.exit();
        


    
