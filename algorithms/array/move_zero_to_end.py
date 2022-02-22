from typing import List


def move_zeroes(nums: List[int]) -> None:
    for i in reversed(range(len(nums))):
        num = nums[i]
        if num == 0:
            del nums[i]
            nums.append(0)
    print(nums)

move_zeroes([0, 0, 1])
