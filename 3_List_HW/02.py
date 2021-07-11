#!/usr/bin/python

'''
	Make a list of ten students in your class. Print the name of each student whose name ends with ‘a’.
'''

students = ['Bibek', 'Dawa', 'David', 'Subash', 'Smaran', 'Renuka', 'Prakash', 'Pramila', 'Samir', 'Durga']

for name in students:
	if (name.endswith("a")):
		print(name)