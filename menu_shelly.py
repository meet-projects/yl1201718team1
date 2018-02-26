import turtle
import time
from ball import Ball

J = turtle.Canvas()
SCREEN_WIDTH = J.winfo_width() / 2
SCREEN_HEIGHT = J.winfo_height() / 2
mouse=Ball(0,0,0,0,10, "blue")

def inst():

	inn=turtle.clone()
	inn.home()
	turtle.clear()
	turtle.addshape("in.gif")
	inn.shape("in.gif")
	inn.stamp()
	turtle.update()
def play():
	turtle.clear()
	turtle.update()

ans = True
turtle.ht()
turtle.tracer(0)
turtle.penup()
turtle.goto (-100,-100)
turtle.write("""
		1. INSTRUCTIONS
		2. PLAY!!




		PRESS 3 TO QUIT
		""",True, align="center", font=("Helvetica", 24, "bold italic"))

def movearound(event):
    x1 = event.x - SCREEN_WIDTH
    y1 = SCREEN_HEIGHT - event.y
    turtle.goto(x1, y1)


turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()



time.sleep(7)

turtle.mainloop()