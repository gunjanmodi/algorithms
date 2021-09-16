def twoNumbersSum(array, target_sum):
	ref_dict = {}
	result = []
	for i in range(len(array)):
		potential_match = target_sum - array[i]
		if potential_match in ref_dict:
			result.append([array[i], potential_match])
		else:
			ref_dict[array[i]] = True
	return result




if __name__ == '__main__':
	array = [3, 5, -4, 8, 11, 1, -1, 6]
	target_sum = 10
	output = twoNumbersSum(array, target_sum)
	print(output)