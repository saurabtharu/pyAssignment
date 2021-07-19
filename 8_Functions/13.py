#!/usr/bin/python

'''
Write a python module with multiple sorting algorithms as its functions
'''

from sorting import *
from random import *



array = [randint(0, 1000) for i in range(10)]


print(f"The unsortedArray is\n\t{array}")

print(f"\nThe sorted array in using bubble sort is:\n\t{bubbleSort(array)}")

print(f"\nThe sorted array in using insertion sort is:\n\t{insertionSort(array)}")

print(f"\nThe sorted array in using merge sort is:\n\t{mergeSort(array)}")