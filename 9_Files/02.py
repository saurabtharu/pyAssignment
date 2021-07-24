#!/usr/bin/python


'''
Make a dictionary of all the unique words and their frequency  in ‘oldman.txt’.

'''


count = dict()
wordslist = list()
# filename = 'text.txt'
filename = 'oldman.txt'
lineList = list()


fo = open(file=filename, mode="r")

for line in fo.readlines():
	word = line.replace('"', '').replace("?", "").replace(".", "").replace(",", '').replace("[",'').replace("]",'').replace("_",'')
	word = word.split()
	for i in word:
		wordslist.append(i)

for word in wordslist:
	if word not in count:				# if the word is not in the dictionary
		count[word] = 1					# if unique word is recognized
	else:								# when the word is already in the dictionary then counter is increased by 1
		count[word] += 1

print(count)
fo.close()




# createFile = open("saurab.txt", "w")
# for words in wordslist:
# 	createFile.write(f"{words}\n")

# for word, freq in count.items():
# 	createFile.write(f"{word},{freq} times\n")
		


# dict={}
# lis=[]
# file =open('oldman.txt')
# for lines in file:
#     word=lines.split()
#     for i in word:
#         lis.append(i)

# print(lis)



# input_file = open("oldman.txt", "r")
# lines = input_file.readlines()
# print("The input file has {0} lines of text.".format(len(lines)))
# print(lines[0])
# for x in range(37, 49):
#     print("{0}: {1}".format(x, lines[x]), end="")
# print("All done!")