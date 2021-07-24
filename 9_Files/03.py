#!/usr/bin/python


'''
Make a dir named ‘Books’. Make 26 directories inside ‘Books’ from A-Z. Put the following files in the following directories.

Files 			Folders
Oldman.txt			O
oliver.txt			O
Alice.txt			A
Siddhartha.txt		S
hitler.txt			H
history.txt			H


'''
'''
import os
from shutil import rmtree
alphabets = ['%c' % (x) for x in range(65, 91)]

fileFolders = {
	"Oldman.txt"		:	"O",
	"oliver.txt"		:	"O",
	"Alice.txt"			:	"A",
	"Siddhartha.txt"	:	"S",
	"hitler.txt"		:	"H",
	"history.txt"		:	"H"
}

# rmtree("Books")							# to remove the folder "Books" recursively
os.mkdir("Books")							# create the directory named "Books"
os.chdir(f"{os.getcwd()}/Books")			# change the directory to "Books"

for i in alphabets:
	os.mkdir(i)
	# rmtree(i)

os.chdir(f"{os.getcwd()}/..")

for files, folders in fileFolders.items():
	with open(file=f"{files}") as orginalFile:				# open a file of same name as give in question
		# strings = orginalFile.read()

		os.chdir(f"{os.getcwd()}/Books/{folders}")			# change the folder to given folders
		newFile = open(file=files,mode="w")				# create a file of same name as given in question   
		newFile.write(orginalFile.read())				# write text read from orginalFile to newFile

	os.chdir(f"{os.getcwd()}/../..")


'''



import os
from posix import listdir
import shutil
import string

main='Books/'
folders=[x for x in string.ascii_uppercase]
for folder in folders:
    os.makedirs(main+folder)

files=['Oldman.txt','oliver.txt','Alice.txt','Siddhartha.txt','hitler.txt','history.txt']
cd=os.getcwd()
for sub_dir in os.listdir('Books'):
    for i in files:
        if sub_dir.lower()==i[0].lower():
            shutil.copy(f'{cd}/{i}',main+sub_dir)