#!/usr/bin/python

'''
users = {
	'g91':{
		'name':'Aron',
		'age':55,
		'poison':'Old monk'
		},
    'twir56':{
		'name':'Visakha',
		'age':26,
		'poison':'coca cola'
		},
	'jsdl8':{
		'name':'Saudi',
		'age':12,
		'poison':'hinwa'
		}
	}
Generate a list of usernames, name, age and poison from the above dictionary.
'''


users = {
	'g91':{
		'name':'Aron',
		'age':55,
		'poison':'Old monk'
		},
    'twir56':{
		'name':'Visakha',
		'age':26,
		'poison':'coca cola'
		},
	'jsdl8':{
		'name':'Saudi',
		'age':12,
		'poison':'hinwa'
		}
	}

usernames = []
name = []
age = []
poison = []

# usernames = [x for x in users.keys()]
# name = [y['name'] for x,y in users.items()]
# age = [y['age'] for x,y in users.items()]
# poison = [y['poison'] for x,y in users.items()]

for key, values in users.items():
	usernames.append(key)
	name.append(values['name'])
	age.append(values['age'])
	poison.append(values['poison'])

print(f"The usernames are:\n\t{usernames}")
print(f"The names are:\n\t{name}")
print(f"The age of people are:\n\t{age}")
print(f"The poisons are:\n\t{poison}")