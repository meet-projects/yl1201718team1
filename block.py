
from turtle import*
colormode(255)

class Block(Turtle):
	def __init__(self, x,y,color,width,height):
		Turtle.__init__(self)
		self.x=x
		self.y=y
		self.penup()
		self.goto(x,y)
		self.shape("square")
		self.shapesize(width,height)#points
		self.color(color)
		self.width = width
		self.height = height
		#1point = 20 pixels

	def top(self):
		return self.ycor()+self.height*10

	def bottom(self):
		return self.ycor()-self.height*10
	
	def right(self):
		return self.xcor()+self.width*10
		
	def left(self):
		return self.xcor()-self.width*10