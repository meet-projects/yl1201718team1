import turtle
import time

def inst(event):

	inn=turtle.clone()
	inn.home()
	turtle.clear()
	turtle.addshape("in.gif")
	inn.shape("in.gif")
	inn.stamp()
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

turtle.getcanvas().bind("<Return>",bye)
turtle.getcanvas().bind("2",play)
turtle.getcanvas().bind("1",inst)
turtle.listen()

turtle.mainloop()