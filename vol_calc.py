#this is to make a volume calculator
import pygame, sys
from pygame.locals import *
print('what is the length')
length = input()
print('what is the width')
width = input()
print('what is the height')
ht = input()
print('calculating')
pygame.time.wait(1000)
print(' volume equals ')
# now to convert the strings into integers
length = int(length)
width = int(width)
ht = int(ht)
print(length * width * ht)
