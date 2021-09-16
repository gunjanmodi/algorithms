def rearrange(nums):
    nums.sort()
    i = j = 1
    while j < len(nums):
        if nums[j] > 0:
            break
        j += 1

    while nums[i] < 0 and j < len(nums):
        nums[i], nums[j] = nums[j], nums[i]

        i += 2
        j += 1

    return nums




# print(rearrange([1, 2, 3, -4, -1, 4])) # [-4, 1, -1, 2, 3, 4]
print(rearrange([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8, -9, -10]))  # [-5, 5, -2, 2, -8, 4, 7, 1, 8, 0]
