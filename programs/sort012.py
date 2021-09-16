def sort012(arr,n):
	low = 0
	mid = 0
	high = n - 1
	for i in range(0, n):
		if arr[i] == 0:
			arr[i], arr[low] = arr[low], arr[i]
			low += 1
			mid += 1
		if arr[i] == 2:
			arr[i], arr[high] = arr[high], arr[i]
			high -= 1
		else:
			mid += 1
	return arr



if __name__ == '__main__':
	arr = [0, 2, 1, 2, 0]
	sort012(arr, 5)