#!/usr/bin/python


'''
Extract all the years (e.g 1994) from the file ‘history.txt’ and save it in another file named ‘year.txt’.

'''

file = "history.txt"
numbers = []
string = ""
with open(file) as histFile:
	string = histFile.read().split()
yearFile = open("year.txt", 'w')

num = 0

for i in string:
	i = i.replace(",", '').replace("(", '').replace(")", '').replace(".", '').replace("–", ' ').replace("[", ' ').replace("]", ' ')
	if i.isnumeric():
		if (len(i)) == 4:
			num+=1
			yearFile.write(f"{num}: {i}\n")