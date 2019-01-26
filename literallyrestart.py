import pygame, sys
#this calculates MPG
print('this program calculates MPG')

miles_driven = input("enter miles driven\n ")
miles_driven = float(miles_driven)
gallons_used = input("enter gallons used\n")
gallons_used = float(gallons_used)
x = miles_driven / gallons_used
print('your MPG =', x)
#running script runner extension w/ atom editor makes this code read exactly
#(your MPG =', 50
