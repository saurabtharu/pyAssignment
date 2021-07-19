#!/usr/bin/python

'''
Write a Python function that accepts a string and calculates the number of uppercase letters and lowercase letters.

'''

def letterCouter(string):
	string = str(string)
	upper = 0
	lower = 0

	for i in string:
		if i == i.lower():
			lower += 1
		else:
			upper += 1
	return upper,lower
	
			
	
string = input("Enter the string: ")
upper, lower =  letterCouter(string)

print(f"There are {upper} uppercase letters and {lower} lowercase letters.")
