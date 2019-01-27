import pygame, sys
from pygame.locals import *

#the goal of this is to take a requested weight in lbs
#and determine how many kilograms/side  the user needs
#to put on the barbell

weight_wanted = int(input("How many pounds are you trying to push?"))
print(" Approx Kilograms per side\n :", ((weight_wanted - 45) / 2.20462) /2)
