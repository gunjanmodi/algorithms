def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        if nums[i] == i + 1:
            i += 1
        else:
            prev = nums[i] - 1
            nums[prev], nums[i] = nums[i], nums[prev]
    return nums


if __name__ == '__main__':
    cyclic_sort([1, 5, 6, 4, 3, 2])