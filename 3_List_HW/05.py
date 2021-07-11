#!/usr/bin/python

'''
	A = ['a',’b’,’c’,’d’] B = ['1’,’a’,’2’,’b’]
	Find  A U B and A intersection B  
'''



A = [ ' a ' , ' b ' , ' c ' , ' d ' ]
B = [ ' 1 ' , ' a ' , ' 2 ' , ' b ' ]


print(f"A = {A}\nB = {B}\n")
union = set(A) | set(B)
print(f"A Union B	 =  {list(union)}")

intersection = set(A) & set(B)
print(f"A Intersection B =  {list(intersection)}")