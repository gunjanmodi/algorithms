def find_missing_number(nums):
    i = 0
    while i < len(nums):
        j = nums[i]
        if nums[i] != i and nums[i] < len(nums):
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    num = 0
    while num < len(nums):
        if nums[num] != num:
            return num
        num += 1
    return -1


if __name__ == '__main__':
    output = find_missing_number([8, 3, 5, 2, 4, 6, 0, 1])
    print(output)