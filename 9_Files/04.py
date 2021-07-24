#!/usr/bin/python


'''
Write a program that asks the user to enter the name of a book. If the book is in your library print its first line. 
If it is not in your library, handle the exception appropriately.

'''

# import os
prompt = "> "


# print("Enter the name of book: ")

while True: 
	print("Enter the name of book: ")
	nameOfBook = input(prompt)
	try:
		with open(nameOfBook) as fo:
			print(f"The first line of the books is:\n\t")
			print(fo.readline())
	except FileNotFoundError:
		print(f"[Error] '{nameOfBook}' is not found in this library")
		break
	

		# try:
		# 	with open(nameOfBook) as fo:
		# 		print(f"The first line of the books is:\n\t")
		# 		print(fo.readline)
		# except:
		# 	print(f"{book} is not found in this library")
	
