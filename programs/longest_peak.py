def longest_peak(array):
	longest_peak_index = 0
	i = 1
	while i < len(array) - 1:

		if not array[i] > array[i - 1] and array[i] < array[i + 1]:
			i += 1
			continue

		left_idx = i - 2
		while left_idx > 0 and array[left_idx] < array[left_idx + 1]:
			left_idx -= 1

		right_idx = i + 2
		while right_idx < len(array) and array[right_idx] > array[right_idx - 1]:
			right_idx += 1
		
		current_peak_length = right_idx - left_idx - 1
		longest_peak_index = max(current_peak_length, longest_peak_index)
	return longest_peak_index

	


if __name__ == '__main__':
	array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
	longest_peak(array)	

