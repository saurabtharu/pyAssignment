#!/usr/bin/python

'''
	Write a program to compute the grade from marks. 
	
	Marks				Grade
	
	Marks<=50			F
	60>=marks>50		E
	70>= marks > 60		D
	80>= marks > 70		C
	90 > = marks > 80	B
	100>= marks >90		A

'''

mark = int(input("Enter the mark: "))

print("F") if (mark <= 50) \
	else print("E") if (mark <= 60) \
		else print("D") if (mark <= 70) \
			else print("C") if (mark <= 80) \
				else print("B") if (mark <= 90) \
					else print("A")