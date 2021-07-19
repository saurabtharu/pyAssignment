#!/usr/bin/python

'''
Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow


'''

def alphabetSorting(text):
	wordList = text.split('-')
	wordList= sorted(wordList)
	string = ""
	j=0
	for i in wordList:
		if j < (len(wordList) -1):
			string += i + '-'
			j += 1
		else:
			string += i
	return string



text = input("Enter the hyphen separated text: ")
# text = "green-red-yellow-black-white-blue-gray-aqua"
print(alphabetSorting(text))
