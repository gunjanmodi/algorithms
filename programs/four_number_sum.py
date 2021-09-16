def fourNumberSum(array, target_sum):
	ref_dict = {}
	result = []
	for i in range(1, len(array) - 1):
		for j in range(i + 1, len(array)):
			current_sum = array[i] + array[j]
			difference = target_sum - current_sum
			if difference in ref_dict:
				for pair in ref_dict[difference]:
					result.append(pair + [ array[i], array[j] ])
		for k in range(0, i):
			current_sum = array[i] + array[k]
			if current_sum not in ref_dict:
				ref_dict[current_sum] = [ [ array[i], array[k]] ]
			else:
				ref_dict[current_sum].append([ array[i], array[k] ])	
	return result

if __name__ == '__main__':
    output = fourNumberSum([7, 6, 4, -1, 1, 2], 16)
    print(output)