def next_permutation(nums):
    i = len(nums) - 1
    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1

    if i == 0:
        nums.reverse()
        return nums

    j = len(nums) - 1
    while nums[j] <= nums[i-1]:
        j -= 1

    nums[i-1], nums[j] = nums[j], nums[i-1]
    nums[i:] = sorted(nums[i:])

    return nums


print(next_permutation([1,2,3,6,5,4])) # [1,2,4,3,5,6]
# print(next_permutation([1,2,3])) # [1,3,2]
# print(next_permutation([3,2,1])) # [1,2,3]
# print(next_permutation([1,1,5])) # [1,5,1]
