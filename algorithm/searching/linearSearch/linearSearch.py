'''
This is the simple implementation of linear search algorithm in python3


'''

def linearSearch(array, size, target):
	for i in range(size):
		if array[i] == target:
			return i
	return -1

if __name__ == "__main__":
	array = [12,34,87,2,83,35,98]
	target1 = 2
	target2 = 30
	print(f"array is {array}")
	print(f"Target 1 is {target1}\nTarget 2 is {target2}") 
	print(f"Result for {target1}: {linearSearch(array, len(array),target1)}\nResult for {target2}: {linearSearch(array, len(array),target2)}\n")

