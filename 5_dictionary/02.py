#!/usr/bin/python

'''
Euro = {‘France’:5,’Germany’:2,’Portugal’:3,’Hungary’:6}
Make two lists from above dictionary
'''

Euro = {'France':5,'Germany':2,'Portugal':3,'Hungary':6}

country = []
goals = []


for key, value in Euro.items():
	country.append(key)
	goals.append(value)

print(f"Give dictionary is\n	{Euro}\n")
print(f"Two lists from given dictionay is\n	{country} \nand\n	{goals}")