def reverse_array(array):
	left_idx = 0
	right_idx = len(array) - 1
	while left_idx < right_idx:
		array[left_idx], array[right_idx] = array[right_idx], array[left_idx]
		left_idx += 1
		right_idx -= 1
	return array


if __name__ == '__main__':
	array = [4, 5, 1, 2]
	reverse_array(array)