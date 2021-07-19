#!/usr/bin/python

'''
Write a Python program to print the even numbers from a given list.

'''

def evenNumbers(l):
	print("Even numbers from the list are: ")
	for i in l:
		if (i % 2 == 0):
			print(i, end="	")
	print("")
li = [2, 3, 4, 5, 6, 22, 23, 13, 12, 14, 16, 39, 99, 92, 94, 92]

evenNumbers(li)