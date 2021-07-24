#!/usr/bin/python


'''
Count the total number of words in ‘oliver.txt’.

'''


from sys import argv 

filename ='oliver.txt'

fh = open(filename)
words = fh.read().split()
print(f"There are {len(words)} words in file {filename}")


fh.close()
