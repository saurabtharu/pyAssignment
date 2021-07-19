#!/usr/bin/python

'''
Show how to calculate the cost of six cartons of milk based on the cost of the milk_carton.
'''


milk_carton = {
	'Nepal dairy': {
				'Expiration_date': (11, 4, 2078),
				'Vol': 55,
				'Cost': 50
	}
}

cost = 0
volume = 0
for value in milk_carton.values():
	cost = value['Cost']
	volume = value['Vol']

noOfCarton = 6
print(f"The cost of {noOfCarton} cartons of milk of Nepal dairy is {noOfCarton*volume*cost}")


