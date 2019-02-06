def countdown(num):
	arr = []
	for i in range(num,-1,-1):
		arr.append(i)
	return arr

def twoNums(arr):
	print(arr[0])
	return arr[1]

def first_plus_length(arr):
	return arr[0] + len(arr)

def values_greater_than_second(arr):
	if len(arr) < 2:
		return False
	else:
		bound = arr[1]
		count = 0
		new_arr = []
		for i in arr:
			if i > bound:
				new_arr.append(i)
				count += 1
		print(count)
		return new_arr

def length_and_value(size, value):
	arr = []
	for i in range(size):
		arr.append(value)
	return arr

