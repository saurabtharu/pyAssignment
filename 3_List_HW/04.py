#!/usr/bin/python

'''
	Change the first alphabet of all elements of the following list to capital.
Bob = [‘hurricane’,’tambourine’,’blowing’,’numb’]

'''

Bob = ['hurricane','tambourine','blowing','numb']
Bob1 = []
print(f"Before changing the first alphabet to capital\nBob = {Bob}\n")

for a in Bob:
	Bob1.append(a.title())

Bob = Bob1
del Bob1
print(f"After changing the first alphabet to capital\nBob = {Bob}\n")