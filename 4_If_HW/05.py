#!/usr/bin/python

'''
	Write a program to check whether the entered year is leap year or not.

'''

year = int(input("Enter the year: "))

print(f"{year} is leap year.") if ((year % 400 == 0) | (year % 4 == 0) & (year % 100 != 0)) else print(f"{year} is not leap year.")
