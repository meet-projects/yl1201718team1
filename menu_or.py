import turtle
import time

def inst(event):
	turtle.clear()
	turtle.goto(250,-250)
	turtle.write("""
		A BRICK WALL APPEARS AT THE SCREEN 
		AND OUR MISSION IS TO SMASH IT-
		ONE BREAK AT A TIME!

		*use the mouse to move the platform
		across the bottom screen

		*across the bottom screen
		each time the ball hits a break, 
		the brick disappears 
		and you score points

		2. PLAY!!

		PRESS ENTER TO QUIT
		""",True, align="right", font=("Helvetica", 15,"bold italic"))
	turtle.update()
def play(event):
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




		PRESS ENTER TO QUIT
		""",True, align="center", font=("Helvetica", 24, "bold italic"))
def bye(event):
	turtle.bye()
for i in range (10000):
	turtle.getcanvas().bind("<Return>",bye)
	turtle.getcanvas().bind("2",play)
	turtle.getcanvas().bind("1",inst)
	turtle.listen()



turtle.mainloop()