def find_duplicate(nums):
    slow, fast = 0, 0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    check = 0
    while True:
        slow = nums[slow]
        check = nums[check]

        if slow == check:
            break

    return check





print(find_duplicate([1,3,4,2,2]))
print(find_duplicate([3,1,3,4,2]))

