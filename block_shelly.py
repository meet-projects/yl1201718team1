from turtle import *
import time
colormode(255)
class Block(Turtle):
	"""docstring for ClassName"""
	def __init__(self, x,y,color,a,b):
		Turtle.__init__(self)
		self.x=x
		self.y=y
		self.a=a
		self.b=b
		self.penup()
		self.goto(x,y)
		self.shape("square")
		self.shapesize(self.a,self.b)
		self.color(color)

time.sleep(2)