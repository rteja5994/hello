#to find areas of the square, circle, sphere

import math

#Square
def area_square(side):

	while True:
		print("Enter 'x' for exit.")
		side = input("Enter side length of Square: ")
		if side == 'x':
			break
		else:
			side_length = int(side)
			area_square = side_length*side_length
			print("Area of Square =",area_square,"\n")
area_square(5)


#circle

def area_circle(radius):
	while True:
		print("Enter 'x' for exit.")
		radius = input("Enter radius of circle: ")
		if radius == 'x':
			break
		else:
			radius_length = float(radius)
			area_circle = 2*math.pi*radius_length
			print("Area of Circle =",area_circle,"\n")
area_circle(3)

#sphere

def area_sphere(radius):
	while True:
		print("Enter 'x' for exit.")
		radius = input("Enter radius of sphere: ")
		if radius == 'x':
			break
		else:
			radius_length = float(radius)
			area_sphere = 4*math.pi*radius_length*radius_length
			print("Area of sphere =",area_sphere,"\n")
area_sphere(3)
