def find_duplicate(nums):
    slow, fast = 0, 0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    fast = 0
    while True:
        slow = nums[slow]
        fast = nums[fast]

        if slow == fast:
            break

    return fast





print(find_duplicate([1,3,4,2,2]))
print(find_duplicate([3,1,3,4,2]))

