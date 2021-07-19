
#!/usr/bin/python


'''
Generate the following patterns using for loop

F
F
FF
FFF
FFFFF
FFFFFFFF
FFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

Fibonacci numbers


'''

rows = int(input("Enter the number of rows: "))

n1 = 1
n2 = 1

for i in range(1, rows + 1):
	if (i == 1 or i == 2):
		print("F",end="")
	else:
		n3 = n1 + n2
		for j in range(n3):
			print("F", end="")
		n1 = n2
		n2 = n3
	print("")
