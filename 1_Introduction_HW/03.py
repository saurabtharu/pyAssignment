#!/usr/bin/python

'''
	Write a Python code that takes the degree as input from the user and convert it into radian
'''

import math

degree = float(input("Enter the value in degree: "))

radian = math.radians(degree)

print(f"The radion of {degree} degree is  {radian}.")

# print(f"The radion of {degree} degree is  %5.2f."%(radian))