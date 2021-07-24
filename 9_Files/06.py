#!/usr/bin/python


'''
Print all the numbers present in ‘hitler.txt’.

'''

file = "hitler.txt"
string = ""
sum = 0
with open(file) as fo:
	string = fo.read().split()

for i in string:
	i = i.replace(",", '').replace("(", '').replace(")", '').replace(".", '').replace("–", ' ').replace("[", ' ').replace("]", ' ')

	if i.isnumeric():
		sum = sum + int(i)

print(sum)