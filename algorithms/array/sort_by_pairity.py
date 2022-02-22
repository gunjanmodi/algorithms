def sort_array_by_parity(nums):
    i = j = 0

    while j < len(nums):
        if nums[j] % 2 == 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1
    return nums


print(sort_array_by_parity([3,1,2,4]))
print(sort_array_by_parity([2,1,3,4]))