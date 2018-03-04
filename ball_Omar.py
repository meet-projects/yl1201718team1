from turtle import *
import random
import math
import time


#tracer(0)
# hideturtle()

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,radius,color):
		Turtle.__init__(self)
		self.pu()
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.shape("circle")
		self.radius=radius
		self.shapesize(radius/10)
		self.color(color)
		
	def top(self):
		return self.ycor()+self.radius/2
		
	def bottom(self):
		return self.ycor()-self.radius/2
	
	def right(self):
		return self.xcor()+self.radius/2
		
	def left(self):
		return self.xcor()-self.radius/2
		
	def move(self,screen_width,screen_height):
		current_x=self.xcor()
		current_y=self.ycor()
		new_x=current_x+self.dx
		new_y=current_y+self.dy
		right_side_ball=new_x+self.radius
		left_side_ball=new_x-self.radius
		top_side_ball=new_y+self.radius
		bottom_side_ball=new_y-self.radius
		right_edge=screen_width
		left_edge=-screen_width
		top_edge=screen_height
		bottom_edge=-screen_height
		self.goto(new_x,new_y)

		if right_side_ball> right_edge:
			self.dx=- self.dx

		elif left_side_ball<left_edge:
			self.dx = -self.dx

		elif top_side_ball>top_edge:
			self.dy= - self.dy 

		elif bottom_side_ball<bottom_edge:
			print("game over")
			write("GAME OVER",True,align="center",font=("Arial",25,"normal"))
			time.sleep(5)
			exit()
			# time.sleep(5)
			self.dy=0
			self.dx=0


			





