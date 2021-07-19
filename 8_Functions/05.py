#!/usr/bin/python

'''
Write a Python function that takes a list and returns a new list with unique elements of the first list


'''

def functionReturningList(l):
	l = set(l)
	return l


fifa = ['Italy','Argentina','Germany','Brazil','France','Brazil','Italy','Spain','Germany','France']

print(f"The given list is:\n {fifa}\n")
fifa = functionReturningList(fifa)

print(f"The new list with unique elements of the previous list is:\n {fifa}")