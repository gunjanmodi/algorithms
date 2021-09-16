def largest_range(array):
	reference_dict = {}
	longest_length = 0
	best_range = []
	for num in array:
		reference_dict[num] = num
	for num in array:
		if not reference_dict[num]:
			continue
		reference_dict[num] = False
		current_length = 1
		left = num - 1
		right = num + 1
		while left in reference_dict:
			reference_dict[left] = False
			current_length += 1
			left -= 1
		while right in reference_dict:
			reference_dict[right] = False
			current_length += 1
			right += 1
		if current_length > longest_length:
			longest_length = current_length
			best_range = [left + 1, right - 1]
	return best_range

if __name__ == '__main__':
	array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
	output = largest_range(array)
	print(output)