#this first program says hello and asks for your name
import pygame, sys
from pygame.locals import *
# anything with a hashtag infront is a "COMMENT LINE". The program skips
# these lines. Usually you want to leave comments in order to explain to
# yourself and others what you're doing. 
print("\n \n Hey, buddy!")
# using \n in a string(a string is just words) creates a new line. You 
# can see this working by the spaces it creates when the program starts up.
pygame.time.wait(2000)
# this tells the program to wait for 2,000 milliseconds (2 whole seconds)
print("\n What's your name?")
yourName = input()
# yourName is now a new variable. Almost like X in an algebraic equation, 
# it can be anything you want. input() is a built-in function to take
# input from the keyboard and collect it when the user presses Enter.
pygame.time.wait(2000)
print("It is nice to meet you, " + yourName)
#we use our new variable here by adding it to the string. 
