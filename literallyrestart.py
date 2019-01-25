import pygame, sys
miles_driven = input("enter miles driven\n ")
gallons_used = input("enter gallons used\n")
#above, you asked the user to input a string. The miles_driven and gallons_used are still strings "number"

#below, you must convert the strings into integers, or floats (if they contain decimals)
# int(miles_driven) will turn a "45" into 45. same with gallons_used
x = miles_driven / gallons_used
print('your MPG =', x)
