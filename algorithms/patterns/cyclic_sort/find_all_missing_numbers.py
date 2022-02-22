def find_all_missing_numbers(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    missing_numbers = []
    print(nums)
    for i in range(len(nums)):
        if nums[i] != i + 1:
            missing_numbers.append(i + 1)


if __name__ == '__main__':
    nums = [2, 3, 1, 8, 2, 3, 5, 1]
    find_all_missing_numbers(nums)