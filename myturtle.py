import turtle
import math
t=turtle.Turtle()
bob=turtle.Turtle()
rob=turtle.Turtle()
"""def square(bob):
	for i in range(4):
		bob.fd(100)
		bob.lt(90)
square(bob)"""

"""def polygon(rob,n,length):
	angle=360.0/n
	for i in range(n):
		rob.fd(length)
		rob.lt(angle)
polygon(rob,8,45)"""

"""def circle(rob,r):
	circumference = 2*math.pi*r
	n=50
	length=circumference/n
	polygon(rob,30,10)
circle(rob,10)"""

def arc(t,r,angle):
	arc_length=2*math.pi*r*angle/360
	n=int(arc_length/3)+1
	step_length=arc_length/n
	step_angle=float(angle)/n
 	
	for i in range(n):
		t.fd(step_length)
		t.rt(step_angle)
arc(t,80,270)
turtle.mainloop()
