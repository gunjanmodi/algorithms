def subsets(nums):
	result = []
	nums.sort()
	visited = [False for _ in nums] 
	backtrack(result, [], nums, visited)
	return result

def backtrack(result, temp_list, nums, visited):
	if len(temp_list) == len(nums):
		result.append(temp_list[:])
		return
	for i in range(len(nums)):
		if visited[i] or i > 0 and nums[i] == nums[i-1] and not visited[i - 1]:
			continue
		visited[i] = True
		temp_list.append(nums[i])
		backtrack(result, temp_list, nums, visited)
		visited[i] = False
		temp_list.pop(-1)


print(subsets([1,1, 2]))