#!/usr/bin/python

'''
	Write a Python code to calculate LCM of (25,55)
'''
import math

num1 = int(input("Enter first numbers: "))
num2 = int(input("Enter second numbers: "))
LCM = math.lcm(num1, num2)

print(f"The LCM of {num1} and {num2} is {LCM}.")