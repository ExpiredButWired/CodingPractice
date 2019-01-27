import random 
import pygame
from tkinter import *
from tkinter import WORD
import tkinter.messagebox


gameIdeas = {	1:"Avoiding Unkillable Objects  There are objects that the player cannot touch. n\These are different from normal enemies because they cannot be destroyed or moved.",
			2:"Instant Death n\ Something causes the player to instantly die, such as spikes or bottomless pits.",
			3:"Game Repeats Until You Die  There is no victory condition in the game, it just keeps going until the player dies. Or, especially with casual games, the game simply repeats after you beat it. (Example: Nibbles, Minefield, Solitare)",
			4:"Remember an Increasing Number of Things  Tests the short-term memory of a player. (Example: Simon)",
			5:"Repeat Pattern  The player must repeat a series of given steps. (Example: Simon Says, Dance Dance Revolution)",
			6:"Forced Constant Movement  The player cannot stand still at any point. (Example: Snake, Rail Shooters, Asteroids, Winter Bells)",
			7:"Block Puzzles  The game involves standard sized objects that must be moved around in a specific way. (Example: Tetris, Sokoban, Connect Four, Dr. Mario, Kirby's Avalanche / Puyo Puyo)",
			8:"Game Keeps Gets Harder Until You Die  Like 'Game Repeats Until You Die' except the difficulty level also keeps increasing. (Example: Tetris)",
			9:"Uncountable Number of Possible Paths  Most games have a few obvious places to go, but this mechanic means that the number of possible ways to order your movement quickly becomes thousands or millions of possible ways and it is not obvious which is the best. (Example: The Traveling Salesman Problem, Sokoban, Flood It, Bloxorz, Mazes)",
			10:"Big Gains for You Can Be Big Gains for Enemy  There is an obvious and easy way to score points, but the more points you take the better position your enemy will be in also. (Example: Othello, Risk)",
			11:"Block Path - You don't directly fight your enemies but instead tried to block their movements. (Example: Tron, Quoridor, Minotaurus, Abalone, Chess (capturing the king))",
			12:"Information Overload - The game presents the player with lots of different variables and pieces of information, and the player must find patterns or make sense of it to make good (or even valid) moves. (Example: Quarto, Set, Bejeweled)",
			13:"Disinformation - The player must try to bluff the opponent into thinking they are stronger (for evasion) or weaker (for traps) than they really are. (Example: Poker, Stratego)",
			14:"Switch Modes - The player needs to constantly switch between two (or more) modes to effectively fight or move. (Example: Ikaruga, Marshie's Malloween Mix-Up, Pacman (switching between running from ghosts to eating them))",
			15:"0Push Mole Down, Mole Pops Up - The moves that the player make will also cause obstacles to appear. Many moves are obviously possible, but the move that does not have negative side effects is not obvious. (Example: Slide Puzzle, Traffic Jam, Lights Out)",
			16:"Cut Off One Head, Two Grow Back - Like 'Push Mole Down, Mole Pops Up' except that making some necessary progress also causes the game to become more difficult. (Example: Asteroids)",
			17:"Bouncing Object - You cannot directly control an object's movement, but can try to direct it so that the environment directs its path. (Example: Pong, Arkanoid)",
			18:"Gravity - Like 'Forced Constant Movement' except objects are pulled either in a certain direction or are pulled towards certain objects. Also consider: zero gravity, reverse gravity, changeable gravity.",
			19:"Mouse Dexterity - The player must move the mouse in a specific way without making errors. Often combined with 'Forced Constant Movement' or 'Avoiding Unkillable Objects'. Keyboard or game controllers usually require this sort of dexterity, but the mouse is usually reserved for either looking around or menu selection (neither of which requires dexterity). (Example: Fruit Ninja, Simon Gesture)",
			20:"Spinning Plates - The player's attention must be split between multiple simultaneous objectives. Often objects need 'recharging' as they deplete at different rates. (Example: Rampart, Diner Dash)",
			21:"Teleports - Rather than moving conventionally, the player can teleport to different parts of the screen. The player may or may not be able to control where the teleport goes.",
			22:"Squad - Rather than a single character, the player controls multiple characters that must work together to achieve an objective. (Example: Syndicate, A Daily Cup of Tea)",
			23:"Scarce Resource - There is an easy way for the player to fight enemies/score points, but it is a scarce resource. The player needs to balance hoarding the resource vs. using them effectively. (Example: Lunar Lander, Many zombie games)",
			24:"Jumping - Almost always combined with gravity, the player must jump from one platform to another and not fall. (Example: Mario)",
			25:"Hidden Image / Where's Waldo? - Like 'Information Overload', but the player is looking at a complex scene for a particular item, clue, or pattern. (Example: Many point-and-click adventure games)",
			26:"Timed - The player must achieve a task within a time limited. Some power ups or achievements can extend the time.",
			27:"Protect a Target - The player must not only stay alive themselves, but protect a target from enemies. The target may or may not be moving. (Example: Missile Command)",
			28:"Undirected Exploration - The player has a large map that they can wander freely around, although obtaining items or solving clues will help open up new areas. The player often backtracks through places. (Example: Cave Story, Metroid, Castlevania)",
			29:"Bullet Hell - The player is surrounded by a very large number of enemies or deadly objects. They are easy to handle individually but difficult in large numbers. (Example: 'Bullet hell' games, many zombie games)",
			30:"Buy Low, Sell High - The game has different items that have changing value. The player must identify when it is good to acquire items when they are plentiful or cheap, and when it is good to sell them when they are scarce or valuable.",
			31:"Brawling - The player's character has several different types of attacks (mostly melee, not ranged) to use against one or multiple enemies. (Example: Street Fighter 2, Double Dragon, River City Ransom)",
			32:"Dialogue Tree - When the player talks to other characters, they select one of many possible things to say. (Example: Many RPGs)",
			33:"Building - The player can place different types of building blocks anywhere in the world to construct objects. (Example: SimCity, Minecraft, Rampart)",
			34:"Race - The player must reach a place before the opponent does. Like 'Timed' except the enemy as a 'timer' can be slowed down by the player's actions, or there may be multiple enemies being raced against."}

root = Tk()
root.geometry("550x400")

def generateIdea(x):
	dice = gameIdeas[random.randint(1,34)]
	return (x.set(dice))
	
def generateNoun():
	with open('nounlist.txt') as f:
		line = f.readlines()
		return (random.choice(line))
		f.close()

def randomizeIdeaOne():
	generateIdea(idea1)
def randomizeIdeaTwo():
	generateIdea(idea2)
def randomizeIdeaThree():
	generateIdea(idea3)
def randomizeOne():
	noun1.set(generateNoun())
def randomizeTwo():
	noun2.set(generateNoun())
def randomizeThree():
	noun3.set(generateNoun())
		
def randomizeAll():
	generateIdea(idea1)
	generateIdea(idea2)
	generateIdea(idea3)
	noun1.set(generateNoun())
	noun2.set(generateNoun())
	noun3.set(generateNoun())
	


noun1 = StringVar()
noun2 = StringVar()
noun3 = StringVar()
idea1 = StringVar()
idea2 = StringVar()
idea3 = StringVar()



ideaOne = Button(root, textvariable = idea1,command = randomizeIdeaOne, bg = "lightgrey", fg = "black", width = 50,wraplength =350, font = ('arial', 10, 'bold')).grid(row = 1, column = 2, sticky="NS")
nounButton1 = Button(root, padx = 16, pady = 16, bd = 8, fg = 'black', width = 5, font = ('arial', 10, 'bold'),
                    textvariable = noun1, bg = 'gray', command = randomizeOne).grid(row = 1, column = 1)

generateIdea(idea1)
noun1.set(generateNoun())

ideaTwo = Button(root, textvariable = idea2, bg = "lightgrey", command = randomizeIdeaTwo, fg = "black", width = 50,wraplength =350, font = ('arial',10, 'bold')).grid(row = 2, column = 2, sticky="NS")
nounButton2 = Button(root, padx = 16, pady = 16, bd = 8,width = 5, fg = 'black', font = ('arial', 10, 'bold'),
                    textvariable = noun2, bg = 'gray', command = randomizeTwo).grid(row = 2, column = 1)

generateIdea(idea2)
noun2.set(generateNoun())

ideaThree = Button(root, textvariable = idea3, bg = "lightgrey", fg = "black", command = randomizeIdeaThree, width = 50,wraplength =350, font = ('arial', 10, 'bold')).grid(row = 3, column = 2, sticky="NS")
nounButton3 = Button(root, padx = 16, pady = 16, bd = 8,width = 5, fg = 'black', font = ('arial', 10, 'bold'),
                    textvariable = noun3, bg = 'gray', command = randomizeThree).grid(row = 3, column = 1)
					
generateIdea(idea3)
noun3.set(generateNoun())

randomizeButton = Button(root, padx=16, pady = 16, bd = 8, fg = "black", font = ('arial', 10, 'bold'),
					text = "RANDOMIZE", bg = 'gold', command = randomizeAll).grid(row = 4, column = 2, sticky = "E")


root.mainloop()