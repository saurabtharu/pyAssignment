#!/usr/bin/python

'''
bird = ['crows','pigeon','eagles','falcon','pigeon','falcon','falcon']
Remove all the duplicates from the following list using while.
'''

bird = ['crows','pigeon','eagles','falcon','pigeon','falcon','falcon']
i = 0
bird1 = []
print(f"The original list of the birds is :\n {bird}")

while i !=len(bird):
	if bird[i] not in bird1:
		bird1.append(bird[i])
	i += 1
bird = bird1
del bird1
print(f"The list of the birds after removing duplicates is :\n {bird}")

