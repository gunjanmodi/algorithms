def combination_sum(nums, target):
    result = []
    backtrack(result, nums, [], target, 0)
    return result

def backtrack(result, nums, temp_list, reamining, start):
    if reamining < 0:
        return
    elif reamining == 0:
        result.append(temp_list[:])
        result.sort()
    else:
        for i in range(start, len(nums)):
            temp_list.append(nums[i])
            backtrack(result, nums, temp_list, reamining-nums[i], i)
            temp_list.pop(-1)



print(combination_sum([7,2,6,5], 16))
print(combination_sum([2,3,6,7], 7))