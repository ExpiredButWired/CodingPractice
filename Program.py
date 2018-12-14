#this first program says hello and asks for your name
import pygame

print("\n \n Hey, buddy!")
pygame.time.wait(2000)
print("What's your name?")
yourName = input()
pygame.time.wait(2000)
print("It is nice to meet you, " + yourName)
