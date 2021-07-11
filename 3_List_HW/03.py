#!/usr/bin/python

'''
	Print all the unique elements in the following list 
	fifa = ['Italy','Argentina','Germany','Brazil','France','Brazil','Italy','Spain','Germany','France']
'''

fifa = ['Italy','Argentina','Germany','Brazil','France','Brazil','Italy','Spain','Germany','France']

uniqueCountries = list(set(fifa))

print(uniqueCountries)
for country in uniqueCountries:
	print(country)