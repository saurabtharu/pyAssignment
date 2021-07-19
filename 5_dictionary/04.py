#!/usr/bin/python

'''
Take the above list and put it in order.
'''

usernames =  ['g91', 'twir56', 'jsdl8']
name = ['Aron', 'Visakha', 'Saudi']
age = [55, 26, 12]
poison = ['Old monk', 'coca cola', 'hinwa']

usernames.sort()
name.sort()
age.sort()
poison.sort()
sortedUsername = sorted(usernames)
sortedName = sorted(name)
sortedAge = sorted(age)
sortedPoison = sorted(poison)


print(f"Sorted username:\n\t{usernames}")
print(f"Sorted name:\n\t{name}")
print(f"Sorted age:\n\t{age}")
print(f"Sorted poison:\n\t{poison}")