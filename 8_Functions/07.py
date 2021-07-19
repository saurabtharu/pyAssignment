#!/usr/bin/python

'''
 Write a Python function to check whether a string is a pangram or not. Note : Pangrams are words or sentences containing every letter of the alphabet at least once.

The quick brown fox jumps over the lazy dog
'''

se = {"%c" % (x) for x in range(97, 123)}
# print(f"se 	= {se}")

def pangrams(string):
	string = set(string.lower())
	
	# print(f"string  = {string}")
	newSet = {x for x in string if x != ' '}
	# print(f"newSet  = {newSet}")

	if se == newSet:
		return True
	else:
		return False

	# for i in string:
	# 	if se <= string:
	# 		return True
	# 	else:
	# 		return False


if pangrams("The quick brown fox jumps over the lazy dog"):
	print("The string is pangrams.")
else:
	print("The string isn't pangrams.")



se = {"%c" % (x) for x in range(97, 123)}

def pangrams(string):
  string = set(string.lower())
  string = {x for x in string if x != ' '}

  if se == string:
    return True
  else:
    return False

if pangrams("The quick brown fox jumps over the lazy dog"):
  print("The string is pangrams.")
else:
  print("The string isn't pangrams.")