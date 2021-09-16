def subarray_sort(array):
	min_out_of_order = float("inf")
	max_out_of_order = float("-inf")
	for i in range(len(array)):
		num = array[i]
		if is_out_of_order(i, num, array):
			min_out_of_order = min(num, min_out_of_order)
			max_out_of_order = max(num, max_out_of_order)
	if min_out_of_order == float("inf"):
		return [-1, -1]
	subarray_left_idx = 0
	while min_out_of_order >= array[subarray_left_idx]:
		subarray_left_idx += 1
	subarray_right_idx = len(array) - 1
	while max_out_of_order <= array[subarray_right_idx]:
		subarray_right_idx -= 1
	return [subarray_left_idx, subarray_right_idx]



def is_out_of_order(i, num, array):
	if i == 0:
		return num > array[i + 1]
	if i == len(array) - 1:
		return num < array[i - 1]
	return num > array[i + 1] or num < array[i - 1]

if __name__ == '__main__':
	array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
	output = subarray_sort(array)
	print(output)