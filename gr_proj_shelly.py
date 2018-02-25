import turtle
import time
import random
from block_shelly import Block
from ball import Ball
import math

turtle.speed(0)


t=20
l=-290
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2
print(SCREEN_HEIGHT, SCREEN_WIDTH)


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

red=random.randint(0,255)
green=random.randint(0,255)
blue=random.randint(0,255)


MY_BALL=Ball(0,-SCREEN_HEIGHT+45,3,3,10, (red,green,blue))
def move_all_balls():
	MY_BALL.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def collide(a,b,c,d):
	y=a.ycor()
	x=a.xcor()
	y2=b.ycor()
	x1=b.xcor()
	sqrt=(y2-y)*(y2-y)+(x1-x)*(x1-x)
	des=math.sqrt(sqrt)
	if(des+10<=c+d):
		return True
	else:
		return False
#if(collide(MY_BALL,platform,MY_BALL.r,-SCREEN_HEIGHT+40)):
	#MY_BALL.dx=-1*MY_BALL.dx
	#MY_BALL.dy=-1*MY_BALL.dy

def movearound(event):
	platform.goto(event.x-SCREEN_WIDTH,-SCREEN_HEIGHT+20)

turtle.getcanvas().bind("<Motion>",movearound)
turtle.getscreen().listen()

while True:
	move_all_balls()


	
turtle.mainloop()