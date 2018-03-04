from turtle import *
import random
import turtle
import time
from block_Omar import Block
from ball_Omar import Ball
import math


tracer(0)



score=0
score_total=turtle.clone()	


t=20
l=-290
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2

		

platform=Block(0,-SCREEN_HEIGHT+20,"black",0.8,7)



BLOCKS=[]
NUMBER_OF_BLOCKS_LINE=9
NUMBER_OF_BLOCKS_COLUMN=10
for i in range(NUMBER_OF_BLOCKS_COLUMN):
	color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
	for g in range(NUMBER_OF_BLOCKS_LINE):

		x=l
		y=SCREEN_HEIGHT-t
		new_block=Block(x,y,color,1,3)
		BLOCKS.append(new_block)

		l=l+70
	t=t+25
	l=-290
# turtle.pu()
# turtle.goto(1000,0)
# turtle.pd()
turtle.ht()

MY_BALL=Ball(0,0,1,1,10,"turquoise")
MY_BALL.goto(0,-SCREEN_HEIGHT+50)

def move_all_balls():
	MY_BALL.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def collision(ball_a,block_a):
	if(
	ball_a.top() >= block_a.bottom() and
	ball_a.right() >= block_a.left() and
	ball_a.bottom() <= block_a.top() and
	ball_a.left() <= block_a.right()
	):
		return True
	else:
		return False

def movearound(event):
	platform.goto(event.x-SCREEN_WIDTH,-SCREEN_HEIGHT+20)

turtle.getcanvas().bind("<Motion>",movearound)
turtle.getscreen().listen()






def ball_plat():
	if collision(platform,MY_BALL)==True:
		print("collided")
		MY_BALL.dy=-(MY_BALL.dy)




	


def check_myball_collision():
	global score , score_total
	for b in BLOCKS:
		if collision(MY_BALL,b) == True:
			print("collided")
			b.hideturtle()
			
				
		
			if score == 10000:
				print("YOU WIN")
				score_total.pu()
				score_total.goto(0,-250)
				score_total.clear()
				score_total.write("SCORE: "+str(score),align="center",font=("Arial",20,"normal"))
				score_total.goto(0,0)
				score_total.write("YOU WIN"+str(score),align="center",font=("Arial",80,"normal"))
				time.sleep(0.9)
				turtle.bye()


			else:
				score+=1 
				score_total.pu()
				score_total.goto(0,-250)
				score_total.clear()
				score_total.write("SCORE: "+str(score),align="center",font=("Arial",20,"normal"))


while True:
	move_all_balls()
	check_myball_collision()
	ball_plat()

	turtle.update()

turtle.write("GAME OVER")

turtle.mainloop()