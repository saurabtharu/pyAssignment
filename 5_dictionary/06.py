#!/usr/bin/python

'''
Print out the values of all of the elements of the milk_carton using the values in the dictionary.
'''


milk_carton = {
	'Nepal dairy ': {
				'Expiration_date': (11, 4, 2078),
				'Vol': 55,
				'Cost': 50
	},
	'Sujal Dairy': {
				'Expiration_date': (11, 4, 2078),
				'Vol': 90,
				'Cost': 49
	},
	'Subash dairy': {
				'Expiration_date': (11, 4, 2078),
				'Vol': 40,
				'Cost': 50
	}
}

print(f"The values are:")
for brand, attributes in milk_carton.items():
	print(f"{brand} =")
	
	for key,value in attributes.items():
		print(f"\t{key}	= {value}")
