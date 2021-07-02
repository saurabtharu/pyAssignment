#!/usr/bin/python

'''
	Write a program to calculate direction and magnitude of the vector described by the following points.
	A = (20,30)
	B = (30,40)
'''

import math

print(f"The given vector are: \nA = (20,30)\nB = (30,40)\n")
x1, y1 = 20, 30
x2, y2 = 30, 40

magnitude = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


'''
for direction 
	tan A = (y2-y1)/(x2-x1)
		A = atan((y2-y1)/(x2-x1))
'''

direction = math.degrees(math.atan((y2 - y1) / (x2 - x1)))

print(f"The magnitude of given vector A and B is: %.4f units\n\
The direction of given vector A and B is: {direction} degree"%(magnitude))