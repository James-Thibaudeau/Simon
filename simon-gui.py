'''James' Simon game - first attempt at creating Simon with a GUI in python
	June 2016
'''

#Imports
import Tkinter
import tkMessageBox
import time
from random import randint

#colour lists for comparison
gameColours = []
playerColours = []

#global count
count = 1

#colour dictionary
colours = {
	1: 'red',
	2: 'blue',
	3: 'yellow',
	4: 'green',
	'red': 'red',
	'blue': 'blue',
	'yellow': 'yellow',
	'green': 'green'
}

#original colours tied to flashed colours
originalcoloursdict = {
	'red': 'darkred',
	'blue': 'darkblue',
	'yellow': 'goldenrod',
	'green': 'darkgreen'
}

#randomly adds a colour to gameColours
def generateColour():
	colour = randint(1,4)
	gameColours.append(colours[colour])

#flashes the colour - 1 second on, 1 second off
def flashColour(colour):
	buttons[colour].config(bg=colours[colour])
	top.update()
	time.sleep(1)
	buttons[colour].config(bg=originalcoloursdict[colour])
	top.update()
	time.sleep(1)

#flashes the colours in the gameColours list
def showColours():
	print gameColours
	for colour in gameColours:
		print 'flashing colour'
		flashColour(colour)

#enables all colour buttons
def enableButtons():
	red.config(state='normal')
	blue.config(state='normal')
	green.config(state='normal')
	yellow.config(state='normal')

#disables all colour buttons
def disableButtons():
	red.config(state='disabled')
	blue.config(state='disabled')
	green.config(state='disabled')
	yellow.config(state='disabled')

#adds colours to the playerColours list
def addColour(colour):
	playerColours.append(colour)
	print playerColours

#compares gameColours to playerColours
def checkColours():
	global gameColours
	global playerColours
	global count
	if gameColours == playerColours:
		count +=1
		tkMessageBox.showinfo("Good Job!", "Good Job! Keep going!")
		playerColours = []
		return True
	else:
		tkMessageBox.showwarning("You Lose!", "You Lose! You reached level %d" %(count))
		playerColours = []
		gameColours = []
		return False

#prompts player to input pattern
def playerInput():
	tkMessageBox.showinfo("Ready?", "Enter the pattern and click check to see your result")
	enableButtons()

#game loop
def game():

	# while True:

	generateColour()
	showColours()
	playerInput()
	
#GUI instance
top = Tkinter.Tk()

#Buttons
red = Tkinter.Button(top, state='disabled', bg="darkred", activebackground="red", height="10", width="10", command= lambda: addColour('red'))
blue = Tkinter.Button(top, state='disabled', bg="darkblue", activebackground="blue", height="10", width="10", command= lambda: addColour('blue'))
green = Tkinter.Button(top, state='disabled', bg="darkgreen", activebackground="green", height="10", width="10", command= lambda: addColour('green'))
yellow = Tkinter.Button(top, state='disabled', bg="goldenrod", activebackground="yellow", height="10", width="10", command= lambda: addColour('yellow'))
start = Tkinter.Button(top, text="start", bg="lightgrey", command=game)
check = Tkinter.Button(top, text="check", bg="lightgrey", command=checkColours)

#dictionary of button objects
buttons = {
	'red': red,
	'blue': blue,
	'yellow': yellow,
	'green': green
}

#button placement
red.grid(row=0, column=0)
blue.grid(row=0, column=1)
green.grid(row=1, column=0)
yellow.grid(row=1, column=1)
start.grid(row=2, column=0)
check.grid(row=2, column=1)

#main
top.mainloop()


