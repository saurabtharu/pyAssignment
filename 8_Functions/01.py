#!/usr/bin/python


'''
Write a function that calculates the X^Y 

'''


def power(b, p):
	"this if a comment for a function"
	if p == 0:
		return 1
	else:
		return b * power(b, p - 1)


print(power(2, 3))
