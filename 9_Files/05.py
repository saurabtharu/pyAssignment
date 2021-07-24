#!/usr/bin/python


'''
Calculate the sum of all numbers that appear after decimal in ‘pi_million_digits.txt’.

'''


file = "pi_million_digits.txt"
sum = 0


with open(file) as piFile:
	for i in piFile.read().replace('.', '').replace('\n', '').replace(" ",''):
		
		sum += int(i)

print(f"The sum of all the numbers that appear after decimal in {file} is {sum-3}")