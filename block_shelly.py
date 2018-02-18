from turtle import *
import time
colormode(255)
class Block(Turtle):
	"""docstring for ClassName"""
	def __init__(self, x,y,color):
		Turtle.__init__(self)
		self.x=x
		self.y=y
		self.penup()
		self.goto(x,y)
		self.shape("square")
		self.shapesize(1,3)
		self.color(color)

time.sleep(2)