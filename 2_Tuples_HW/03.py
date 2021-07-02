#!/usr/bin/python

'''
	Write a program to demonstrate data types that can be elements of a tuple.
'''

myTuple = (23, "car", 'A', ["twitter", "linkedIn", "reddit"], {23, 34, 55})


i = 0
for dataType in myTuple:
	print(f"[*] {myTuple[i]} = {type(dataType)}")
	i+=1