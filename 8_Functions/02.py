#!/usr/bin/python


'''
Write a Python function to multiply all the numbers in a list.

'''

numbers = [3, 4, 2, 1, 2, 3, 4]

def multiplication(l):
	mult= 1
	for i in numbers:
		mult *= i
	return mult

print(f"The product of all the elements of the list is {multiplication(numbers)}")