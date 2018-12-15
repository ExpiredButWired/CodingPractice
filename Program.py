#lets try something new
import pygame, sys
from pygame.locals import *
# anything with a hashtag infront is a "COMMENT LINE". The program skips
# these lines. Usually you want to leave comments in order to explain to
# yourself and others what you're doing.
print("\n \n Hey, Marcus!")
# using \n in a string(a string is just words) creates a new line. You
# can see this working by the spaces it creates when the program starts up.
pygame.time.wait(2000)
# this tells the program to wait for 2,000 milliseconds (2 whole seconds)
print("\n What number, between 0 and 10 am I thinking of?")
numberguess = input()
# yourName is now a new variable. Almost like X in an algebraic equation,
# it can be anything you want. input() is a built-in function to take
# input from the keyboard and collect it when the user presses Enter.
pygame.time.wait(2000)
print("You guessed " + numberguess + ' right?' )
pygame.time.wait(3000)
print("THIS MESSAGE WILL SELF DESTRUCT IN...")
print("10")
pygame.time.wait(1000)
print("9")
pygame.time.wait(1000)
print("8")
pygame.time.wait(1000)
print("7")
pygame.time.wait(1000)
print("6")
pygame.time.wait(1000)
print("5")
pygame.time.wait(1000)
print("4")
pygame.time.wait(1000)
print("3")
pygame.time.wait(1000)
print("guess again to save the world")
secondguess = input()
pygame.time.wait(1000)
print('The world needed you to guess anything but ' + secondguess + '.')
pygame.time.wait(4000)
print('WE COUNTED ON YOU..')
pygame.time.wait(1000)
print("2")
print("1")
pygame.time.wait(3000)
print("BOOM")
