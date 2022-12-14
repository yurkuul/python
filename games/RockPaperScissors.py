# -*- coding: utf-8 -*-

import random

"""
A rock paper scissors game.

@author: LZ-FSDev
@Python version: Python 3.9
@version: 0.0.5
"""

print("Welcome to rock paper scissors!")
print()

userChoice = ""
#to hold on to the choices available
choices = ["Rock", "Paper", "Scissors"]

#grab user's choice
userChoice = input("Please type in console what you would like to go: ")
print()

#prompt for user's choice if user input is invalid
while (userChoice not in choices):
    print()
    print("That is not a valid option!")
    userChoice = input("Please type in console what you would like to go: ")

print()
print("Rock, Paper, Scissors!")
print()

#generating random int between 0 and 2 inclusive
randomNumber = random.randint(0,2)

#setting a random choice
randomChoice = choices[randomNumber]

#print out computer and user choices
print("Computer: {} \nUser: {}".format(randomChoice, userChoice))
print()

#check if user wins, loses, or ties against computer
if (userChoice == "Scissors"):
    if (randomChoice == "Paper"):
        print("You win")
    elif (randomChoice == "Rock"):
        print("You lose")
    elif (randomChoice == "Scissors"):
        print("It's a tie")
elif (userChoice == "Rock"):
    if (randomChoice == "Scissors"):
        print("You win")
    elif (randomChoice == "Paper"):
        print("You lose")
    else:
        print("It's a tie")
else:
    if (randomChoice == "Scissors"):
        print("You lose")
    elif (randomChoice == "Rock"):
        print("You win")
    else:
        print("It's a tie")
