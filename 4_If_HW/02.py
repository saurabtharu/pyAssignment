#!/usr/bin/python

'''
	Write a python program to check whether a character is uppercase or lowercase alphabet.

'''
a = input("Enter a character: ")

print(f"{a} is Lowercase") if (a.islower()) else print(f"{a} is Uppercase") if (a.isupper()) else print("Invalid input!!")
