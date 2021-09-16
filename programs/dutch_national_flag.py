def dutch_national_flag(arr):
	low, i = 0, 0
	high = len(arr) - 1
	while i <= high:
		if arr[i] == 0:
			arr[i], arr[low] = arr[low], arr[i]
			low += 1
			i += 1
		if arr[i] == 1:
			i += 1
		if arr[i] == 2:
			arr[i], arr[high] = arr[high], arr[low]
			high -= 1
	return arr

if __name__ == '__main__':
	output = dutch_national_flag([2, 2, 0, 1, 2, 0])
	print(output)