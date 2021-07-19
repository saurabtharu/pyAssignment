from random import  *


def bubbleSort(array):
	"takes list as arguments and return the sorted list"
	n = len(array)

	for i in range(n):
		for j in range(n - i - 1):
			if array[j] > array[j + 1]:
				temp = array[j + 1]
				array[j + 1] = array[j]
				array[j] = temp
	

	return array



def insertionSort(array):
    for i in range(1, len(array)):
        key_item = array[i]

        j = i - 1

        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item

    return array


def merge(left, right):
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def mergeSort(array):
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    return merge(
        left=mergeSort(array[:midpoint]),
        right=mergeSort(array[midpoint:]))


