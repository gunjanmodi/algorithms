def combination_sum(nums, target):
    result = []
    nums.sort()
    backtrack(result, nums, [], target, 0)
    return result   

def backtrack(result, nums, temp_list, reamining, start):
    if reamining < 0:
        return
    elif reamining == 0:    
        result.append(temp_list[:])
    else:
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            temp_list.append(nums[i])
            backtrack(result, nums, temp_list, reamining-nums[i], i + 1)
            temp_list.pop(-1)


print(combination_sum([10,1,2,7,6,1,5], 8))