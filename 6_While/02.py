#!/usr/bin/python


'''
Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. 
Then make an empty list called finished_sandwiches . Loop through the list of sandwich orders
and print a message for each order, such as I made your tuna sandwich. As each sandwich is made,
move it to the list of finished sandwiches. After all the sandwiches have been made, print a message
listing each sandwich that was made.
'''

sandwich_orders = ['American sub', 'Bacon', 'Bagel toast', 'Baked bean', 'Bologna salad', 'Carrozza', 'Chicken schnitzel']

finished_sandwiches = []

while sandwich_orders:
	ordered_sandwich = sandwich_orders.pop(0)
	print(f"I made your {ordered_sandwich} sandwich")
	finished_sandwiches.append(ordered_sandwich)
print("")

print(f"All the ordered sandwiches are:")
i = 0
while i != len(finished_sandwiches):
	print(f"	{finished_sandwiches[i]}")
	i+=1