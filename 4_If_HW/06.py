#!/usr/bin/python

'''
	Write a program to check if the number is Armstrong or not.

'''

num = input("Enter a number: ")
len = len(num)

num = int(num)
a = num
result = 0

a = num
for i in range(0, len):
	rem = a % 10
	a = int(a / 10)
	result += pow(rem, len)

print(f"{num} is Armstrong") if(num == result) else print(f"{num} is not Armstrong")
