#!/usr/bin/python

'''
	Make a list of ten students in your class. Print the name of each student whose name starts with ‘B’.
'''

students = ['Bibek', 'Badal', 'David', 'Subash', 'Smaran', 'Thaneshwor', 'Prakash', 'Rahul', 'Samir', 'Bigesh']

for name in students:
	if (name.startswith("B")):
		print(name)