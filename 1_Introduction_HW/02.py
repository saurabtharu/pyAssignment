#!/usr/bin/python

'''
	Write a Python code to calculate Combination (15,3)

'''

'''
	combintaion = 15!/((15-3)! * 3!)
'''

import math
combination = math.comb(15, 3)


print(f"The combination of (15,3) is %d"%(combination))