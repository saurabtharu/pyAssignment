#!/usr/bin/python

'''
	Calculate the mean and standard deviation of the following list:
	Numbers = [1,2,3,5,88,99,55,33,41,52]

'''


Numbers = [1,2,3,5,88,99,55,33,41,52]

mean = sum(Numbers) / len(Numbers)
print(f"Mean = {mean}")

standardDeviation = (sum([(x - mean) ** 2 for x in Numbers]) / len(Numbers)) ** (1 / 2)

print(f"Standard Deviation = %3.2f"%(standardDeviation))