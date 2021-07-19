#!/usr/bin/python

'''
 
Multiply following matrices


	111	22	33	44 
A =	44	55	66	1
	47	86	19	2
	1	22	22	3
 


	11	22	3	4
B =	4	5	6	1
	7	6	19	2
	1	2	22	3

Using for loops and print the result

'''

A  =[
		[111, 22, 33, 44], 
		[44, 55, 56, 1], 
		[47, 86, 19, 2], 
		[1, 2, 22, 3]
	]

B = [
		[11, 22, 3, 4], 
		[4, 5, 6, 1], 
		[7, 6, 19, 2], 
		[1, 2, 22, 3]
	]


# resMatrix = [[0 for x in range(len(A))] for y in range(len(B[0]))] 
resMatrix = [
				[0, 0, 0, 0],
				[0, 0, 0, 0],
				[0, 0, 0, 0],
				[0, 0, 0, 0]
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