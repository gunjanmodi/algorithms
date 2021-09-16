def max_sub_array_of_size_k(K, arr):
	current_sum = 0
	window_start = 0
	max_sum = 0
	for window_end in range(len(arr)):
		current_sum += arr[window_end]
		if window_end >= K - 1:
			max_sum = max(current_sum, max_sum)
			current_sum -= arr[window_start]
			window_start += 1
	return max_sum


if __name__ == '__main__':
	output = max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])
	print(output)