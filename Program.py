#lets try something new
import pygame, sys, random #I imported random in order to create random numbers
from pygame.locals import *


print("\n \n Hey, Bryant!")
pygame.time.wait(2000)

print("\n What number, between 0 and 20 am I thinking of? \n You have 5 chances")
minValue = 1
maxValue = 20
myRandomNumber = random.randint(minValue,maxValue) #create a random number between 1 and 20, and store it in the variable myRandomNumber
x = 0
while x < 5: #creating a loop to repeat the process until x == 5

	numberguess = input("\n You've guessed " + str(x) + " times. \n Try to guess my number: ") #right now, we receive the input as a string.
	pygame.time.wait(1000)

	print("\n You guessed " + numberguess + ', right?' ) #this allows us to concatenate these 3 strings together.

	pygame.time.wait(1000)
	if int(numberguess) == myRandomNumber:
		print("\n You guessed the correct number! Good Job!")
		break #Once you guess the right number, the loop is broken, and continues the rest of the code.
	elif int(numberguess) < minValue:
		print("\n Your number isn't within the range!")
	elif int(numberguess) > maxValue:
		print("\n Your number isn't within the range!")
	elif int(numberguess) > myRandomNumber: #HOWEVER, this is comparing numbers, so we had to convert numberguess into an integer
		print("\n Your number is too high")
		x = x+1
	elif int(numberguess) < myRandomNumber:
		print("\n Your number is too low")
		x = x+1
pygame.time.wait(2000)

if x == 5:
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
	print('The world needed you to guess anything but ' + numberguess + '.')
	pygame.time.wait(1000)
	print('WE ALL COUNTED ON YOU..')
	pygame.time.wait(1000)
	print("2")
	pygame.time.wait(1000)
	print("1")
	pygame.time.wait(1000)
	print("BOOM!")
	pygame.time.wait(5000)
else:
	print("You saved the world! \n Goodbye!")
	pygame.time.wait(5000)
