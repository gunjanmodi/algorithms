def subsets(nums):
	result = []
	backtrack(result, [], nums)
	return result

def backtrack(result, temp_list, nums):
	if len(temp_list) == len(nums):
		result.append(temp_list[:])
	else:
		for i in range(len(nums)):
			if not nums[i] in temp_list:
				temp_list.append(nums[i])
				backtrack(result, temp_list, nums)
				temp_list.pop(-1)


print(subsets([1,2,3]))
print(subsets([1,2,3,4]))
