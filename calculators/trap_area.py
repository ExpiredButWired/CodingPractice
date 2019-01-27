import pygame, sys
from pygame.locals import *

#this is to calcualate the area of a trapezoid
# formual = A= 1/2 (x1 + x2)h

print(" This will calculate the area of a trapezoid")
height = float(input("Enter the height\n"))
base_1 = float(input("Enter the length of the top base\n"))
base_2 = float(input("Enter the length of the bottom base\n"))
print("Area Equals: ", (.5) * ((base_1 + base_2) * height))
