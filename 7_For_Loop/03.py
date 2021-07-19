
#!/usr/bin/python


'''
Generate the following patterns using for loop


F
FFF
FFFFF
FFFFFFF
FFFFFFFFF
FFFFFFFFFFF

'''

rows = int(input("Enter the number of rows: "))

for i in range(1,rows+1):
	for j in range(2 * i - 1):
		print('F',end="")
	print("")