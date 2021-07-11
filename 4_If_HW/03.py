#!/usr/bin/python

'''
	WAP to find whether given input is number or character.

'''

aa = input("Enter the input: ")

print(f"{aa} is character ") if(aa.isalpha()) else print(f"{aa} is number") if(aa.isalnum()) else print("invalid input")