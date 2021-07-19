#!/usr/bin/python

'''
Multiply following matrices

	1	2	3	
A =	4	5	6 
	7	8	9

	111	22	33 
A =	44 	55	56 
	47	86	19
Using for loops and print the result

'''

A = [
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]
	]
B = [
		[111, 22, 33],
		[44, 55, 56],
		[47, 86, 19]	
	]


# resMatrix = [[0 for x in range(len(A))] for y in range(len(B[0]))]

resMatrix = [
				[0, 0, 0],
				[0, 0, 0],
				[0, 0, 0]
			] 


'''
printing matrix A
'''
print("The matrix  A is: ")
for i in range(len(A)):
	for j in range(len(A[i])):
		print(f"	{A[i][j]}",end="	")
	print("")
print("")

'''
printing matrix B
'''
print("The matrix  B is: ")

for i in range(len(B)):
	for j in range(len(B[i])):
		print(f"	{B[i][j]}",end="	")
	print("")

print("")

for i in range(len(A)):
	for j in range(len(A[i])):
		for k in range(len(B[i])):
			resMatrix[i][j] += A[i][k] * B[k][j]

'''
printing resultant  matrix 
'''
print("The resultant matrix is : ")

for i in range(len(resMatrix)):
	for j in range(len(resMatrix[i])):
		print(f"	{resMatrix[i][j]}",end="	")
	print("")





# comments
''' comments '''


''''
A = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
	]
B = [
	[111, 22, 33],
	[44, 55, 56],
	[47, 86, 19]	
	]
resMatrix = [[0 for x in range(3)] for y in range(3)] 


for i in range(len(A)):
	for j in range(len(A[i])):
		print(f"{A[i][j]}",end=" ")
	print("")
print("")

for i in range(len(B)):
	for j in range(len(B[i])):
		print(f"{B[i][j]}",end=" ")
	print("")

print("")

for i in range(3):
	for j in range(3):
		for k in range(3):
			resMatrix[i][j] += A[i][k] * B[k][j]

print("The resultant matrix is : ")

for i in range(len(resMatrix)):
	for j in range(len(resMatrix[i])):
		print(f"{resMatrix[i][j]}",end=" ")
	print("")

'''

