#!/usr/bin/python

'''
	Write a Python code to calculate Permutation (5,3)
'''
import math

'''
	permutation = 5!/(5-3)!
'''

permutation = math.perm(5,3)
print(f"The permutation of (5,3) is %d" % (permutation))
