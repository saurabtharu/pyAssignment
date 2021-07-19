#!/usr/bin/python


'''
Write a Python program to access a function inside a function

'''
def func1(name, age):
	i = 2	
	def func2():
		print(f"{name} is {age} years old.")
	print(f"type of func = {type(func2)}")
	return func2


name = input("Enter your name: ")
age = int(input("Enter your age: "))
a = func1(name, age)
a()
