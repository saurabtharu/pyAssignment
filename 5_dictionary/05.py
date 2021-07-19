#!/usr/bin/python

'''
Create an empty dictionary called milk_carton. Add the following key/value pairs.You can make up the values or use a real milk carton.
	Expiration_date: a tuple with day, month, year
	Vol: volume of milk 
	Cost: cost of milk
	Brand_name
'''
milk_carton = dict()


while True:
	brand_name = input("Enter the brand name: ")
	print("\nEnter Expiration date of milk: ")
	day = int(input("\tEnter the day: "))
	month = int(input("\tEnter the month: "))
	year = int(input("\tEnter the year: "))

	vol = int(input("\tEnter the volume: "))
	cost = int(input("\tEnter the cost: "))
	

	milk_carton.update({brand_name: {'Expiration_date': (day, month, year), 'Vol':vol, 'Cost': cost}})

	print("")
	flag = input("Want to continu??[yes/no] ")
	if flag != 'yes':
		break
	

print(milk_carton)