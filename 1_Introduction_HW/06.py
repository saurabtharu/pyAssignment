#!/usr/bin/python

'''
	Ask enter to enter two numbers (say, a and b). Generate two random numbers between those 
	two numbers and find a combination of these two newly generated random numbers. 

'''
import math
import random

a = float(input("Enter a: "))
b = float(input("Enter b: "))

rand1 = random.randint(a, b)
rand2 = random.randint(a, b)

print(f"The two random numbers between {a} and {b} are %d and %d " % (rand1, rand2))


if (rand1 < 0 or rand2 < 0):
	exit
elif (rand1 > rand2):
	combination = math.comb(rand1, rand2)
	print(f"The combination of ({rand1},{rand2}) is %d"%(combination))
else:
	combination = math.comb(rand2, rand1)
	print(f"The combination of ({rand2},{rand1}) is %d"%(combination))
	