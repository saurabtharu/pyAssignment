#!/usr/bin/python

'''
	Convert tuples to list.
'''


myTuple = ("Ram", "Hari", "Shyam", "Gita", "Sita")
print(f"type(mytuple) = {type(myTuple)}\nand the myTuple: {myTuple}\n")

myTuple = list(myTuple)

print(f"type(mytuple) = {type(myTuple)}\nand the myTuple: {myTuple}")