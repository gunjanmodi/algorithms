def subsets(nums):
	result = []
	backtrack(result, [], nums, 0)
	return result

def backtrack(result, temp_list, nums, start):
	result.append(temp_list[:])
	for i in range(start, len(nums)):
		temp_list.append(nums[i])
		backtrack(result, temp_list, nums, i + 1)
		temp_list.pop(-1)

print(subsets([1,2,3]))
print(subsets([1,2,2]))
    