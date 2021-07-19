#!/usr/bin/python


'''
Write a Python program to reverse a string.


'''

def reverseString(text):
	reverse = ""
	i = len(text)-1

	while i >= 0:
		reverse += text[i]
		i -= 1
	print(reverse)
		

text = input("Enter the string: ")

reverseString(text)