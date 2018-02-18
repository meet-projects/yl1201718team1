import turtle
import time
import random
from block import Block
import math

turtle.speed(0)


t=20
l=-290
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2


platform=turtle.clone()
platform.penup()
platform.shape("square")
platform.shapesize(0.8,7)
platform.goto(0,-SCREEN_HEIGHT+20)

BLOCKS=[]
NUMBER_OF_BLOCKS_LINE=9
NUMBER_OF_BLOCKS_COLUMN=10
for i in range(NUMBER_OF_BLOCKS_COLUMN):
	color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
	for g in range(NUMBER_OF_BLOCKS_LINE):
		x=l
		y=SCREEN_HEIGHT-t
		new_block=Block(x,y,color)
		BLOCKS.append(new_block)
		l=l+70
	t=t+25
	l=-290

def movearound(event):
	platform.goto(event.x-SCREEN_WIDTH,-SCREEN_HEIGHT+20)

turtle.getcanvas().bind("<Motion>",movearound)
turtle.getscreen().listen()

	
turtle.mainloop()