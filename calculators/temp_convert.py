import pygame, sys
from pygame.locals import *

print("Hey, temps are different, \'round the world")
#id like to have it ask which way they want to convert the temps
# and convert it the way the client asks
print("this will convert Fahrenheit to Celsius ")

fahrenheit_temp = int(input("What is the temperature in Farenheit?\n"))
print((fahrenheit_temp - 32) * 5/9)
