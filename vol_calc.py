#this is to make a volume calculator
import pygame, sys
from pygame.locals import *

while True:
	try:
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
		answer = length * width * ht
		if answer > 0:
			print(answer)
			pygame.time.wait(2000)
			break
	except ValueError:
		print("\n \n \n OOPS.")
		print("Make sure to use numbers, and not letters or special characters!\n Try again.\n \n ")
