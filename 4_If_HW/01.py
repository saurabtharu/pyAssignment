#!/usr/bin/python

'''
	Write a python program to find the largest of three numbers .
'''


a, b, c = 45, 34, 65

largest = a if (a > b and a > c) else b if (b > c) else c

print(f"Largest = {largest}")