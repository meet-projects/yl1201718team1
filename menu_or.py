import turtle
import time

def inst():

	inn=turtle.clone()
	inn.home()
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




		PRESS ENTER TO QUIT
		""",True, align="center", font=("Helvetica", 24, "bold italic"))

#turtle.onkey(inst(),"<1>")
#turtle.onkey(play(),"<2>")
#turtle.onkey(turtle.bye(),"<Enter>")
time.sleep(7)

turtle.mainloop()