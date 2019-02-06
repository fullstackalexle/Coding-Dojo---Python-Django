def biggie_size(arr):
	for i in range(0,len(arr)):
		if arr[i] > 0:
			arr[i] = "big"
	return arr

def count_positives(arr):
	count = 0
	for i in arr:
		if i > 0:
			count += 1
	arr[-1] = count
	return arr

def sum_total(arr):
	total = 0
	for i in arr:
		total += i
	return total

def average(arr):
	total = 0
	avg = 0.0
	for i in arr:
		total += i
	avg = total / len(arr)
	return avg

def length(arr):
	count = 0
	for i in arr:
		count += 1
	return count

def minimum(arr):
	if len(arr) < 1:
		return False
	mini = arr[0]
	for i in range(1,len(arr)):
		if arr[i] < mini:
			mini = arr[i]
	return mini

def maximum(arr):
	if len(arr) < 1:
		return False
	maxi = arr[0]
	for i in range(1,len(arr)):
		if arr[i] > maxi:
			maxi = arr[i]
	return maxi

def ultimate_analysis(arr):
	if len(arr) < 1:
		return False
	mini = arr[0]
	maxi = arr[0]
	total = arr[0]
	avg = 0.0
	for i in range(1,len(arr)):
		if arr[i] < mini:
			mini = arr[i]
		elif arr[i] > maxi:
			maxi = arr[i]
		total += arr[i]
	avg = total / len(arr)
	return {"sumTotal": total, "average": avg, "minimum": mini, "maximum": maxi, "length": len(arr) }

def reverse_list(arr):
	for i in range(0,int(len(arr)/2)):
		temp = arr[i]
		arr[i] = arr[len(arr) - 1 - i]
		arr[len(arr) - 1 - i] = temp
	return arr

