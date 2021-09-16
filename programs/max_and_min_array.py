def get_min_and_max(array):
	min_val = float("inf")
	max_val = float("-inf")

	for num in array:
		if num > max_val:
			max_val = num
		if num < min_val:
			min_val = num
	print([min_val, max_val])
	return [min_val, max_val]

if __name__ == '__main__':
	array = [1000, 11, 445, 1, 330, 30000]
	get_min_and_max(array)