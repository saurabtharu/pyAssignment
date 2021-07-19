#!/usr/bin/python

'''
Write three different functions to calculate the mean, variance and standard deviation of the following data.
You need to call your mean function to within your variance and standard deviation functions.

S.N 		Students 		Marks
1			Richard			24
2			Lara			36			
3			Prava			45
4			Peter			45
5			Judas			96
6			Jimmy			56
7			Jimi			89
8			Ronaldo			12
9			Messi			10
10			Pogba			100
'''


def mean(array):
	sum = 0
	for i in array:
		sum += i
	meanValue = sum / len(array)
	return meanValue

def standardDeviation(array):
	SD = (sum([(x - mean(array)) ** 2 for x in array]) / len(array)) ** (1 / 2)
	return SD
	
def variance(array):
	variance = pow(standardDeviation(array), 2)
	return variance

marks = {24, 36, 45, 45, 96, 56, 89, 12, 10, 100}

print(f"The mean of given data is:\n\t%.3f"%(mean(marks)))
print(f"The standard deviation of given data is:\n\t%.3f"%(standardDeviation(marks)))
print(f"The variance of given data is:\n\t%.3f"%(variance(marks)))
