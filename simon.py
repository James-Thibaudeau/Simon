#James' Simon game - text based Simon
from random import randint
import time
import os

gameColours = []
playerColours = []

colours = {
	1: 'red',
	2: 'blue',
	3: 'yellow',
	4: 'green'
}

#clears screen
def cls():
	os.system('cls' if os.name=='nt' else 'clear')

#randomly generates a colour and adds it to the pattern
def generateColour():
	colour = randint(1,4)
	gameColours.append(colours[colour])

#shows the pattern
def showColours():
	for colour in gameColours:
		cls()
		print colour
		time.sleep(1)

#takes the player input and sets it to the player colours
def playerInput():
	cls()
	playerIn = raw_input("Enter the colours you saw in order (separate them by spaces): ")
	global playerColours 
	playerColours = playerIn.split()
		
def game():
	
	count = 1
	print "Welcome to James' Simon Game"
	ready = raw_input("Are you ready to play? (y/n): ")
	
	while(True):

		if ready.lower() == 'n':
			print "Goodbye!"
			break
		
		generateColour()
		showColours()
		playerInput()
		
		if gameColours == playerColours:
			count += 1
			print "Get ready for round %d" % (count)
			raw_input("Press any key to continue")
		else:
			print "You lose! You got %d rounds in!" % (count)
			break

game()
	
