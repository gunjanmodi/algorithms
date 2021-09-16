def is_monotonic(array):
	is_increasing = True
	is_decreasing = True

	for i in range(1, len(array)):
		if array[i - 1] > array[i]:
			is_decreasing = False
		elif array[i - 1] < array[i]:
			is_increasing = False
	return is_increasing or is_decreasing




if __name__ == '__main__':
	array = [-1, 6, -10, -1100, -1100, -1101, -1102, -9001]
	# array = []
	# array = [1]
	# array = [1, 2, 0]
	# array = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10, 11]
	print(is_monotonic(array))
