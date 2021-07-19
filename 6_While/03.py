#!/usr/bin/python

'''
Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit 
one place in the world, where would you go? Include a block of code that prints the results of the poll.
'''

polls = {}

while True:
	name = input("What is your name? ")
	dream_vacation = input("If you could visit one place in the world, where would you go? ")

	polls[name] = dream_vacation
	print("")
	
	respond = input("Others also should give a poll?? [yes/no] ")
	print("*******************************************************************\n")
	if respond != "yes":
		break

print("Result\n---------")
for name, place in polls.items():
	print(f"{name}'s dream place to visit is {place}.")