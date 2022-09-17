# -*- coding: utf-8 -*-

import random

"""
A rock paper scissors game.

@author: LZ-FSDev
@Python version: Python 3.9
@version: 0.0.2
"""

print("Welcome to rock paper scissors!")
print()

userChoice = ""
choices = ["Rock", "Paper", "Scissors"]

userChoice = input("Please type in console what you would like to go: ")
print()

while (userChoice not in choices):
    print()
    print("That is not a valid option!")
    userChoice = input("Please type in console what you would like to go: ")

print()
print("Rock, Paper, Scissors!")
print()

#generating random int between 0 and 2 inclusive
randomChoice = random.randint(0,2)

print("Computer: {} \nUser: {}".format(choices[randomChoice], userChoice))
