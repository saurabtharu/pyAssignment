#!/usr/bin/python

'''
	Write a program to check whether the input alphabet is vowel or not using if-else.

'''
aa = input("Enter the input: ")

vowel = ['a','e','i','o','u','A','E','I','O','U']

print(f"{aa} is vowel") if (aa in  vowel) else print(f"{aa} is not vowel")
