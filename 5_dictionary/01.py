#!/usr/bin/python

'''
Students = ['jack','jill','david','silva','ronaldo']
Marks = ['55','56','57','66','76']
Make a dictionary using lists above and delete the key-value (students:marks) pairs with lowest marks. 

'''
Students = ['jack','jill','david','silva','ronaldo']
Marks = [ ' 55 ' , ' 56 ' , ' 57 ' , ' 66 ' , ' 76 ' ]

marksDict = dict()

for i in range(len(Students)):
	marksDict[Students[i]] = Marks[i]

print(f"The students:marks dictionary is\n\t {marksDict}")
for key, value in marksDict.items():
	if value == min(marksDict.values()):
		marksDict.pop(key)
		break
print("\nAfter delete the key-value (students:marks) pairs with lowest marks\n")
print(f"The students:marks dictionary is\n\t {marksDict}")
