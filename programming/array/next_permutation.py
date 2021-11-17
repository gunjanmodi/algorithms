"""
Find next permutation
Solution explained at: https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
Algorithm:
Firstly, identify the longest suffix that is non-increasing (i.e. weakly decreasing).
In our example, the suffix with this property is (5, 3, 3, 0).


"""
def next_permutation(nums):
    # To find next permutations, we'll start from the end
    i = len(nums) - 1
    # First we'll find the first non-increasing element starting from the end
    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1
    # After completion of the first loop, there will be two cases
    # 1. Our i becomes zero (This will happen if the given array is sorted decreasingly).
    # In this case, we'll simply reverse the sequence and will return
    if i == 0:
        nums.reverse()
        return nums
    # 2. If it's not zero then we'll find the first number grater than nums[i-1] starting from end
    j = len(nums) - 1
    while nums[j] <= nums[i - 1]:
        j -= 1
    # Now out pointer is pointing at two different positions
    # i. first non-assending number from end
    # j. first number greater than nums[i-1]

    # We'll swap these two numbers
    nums[i - 1], nums[j] = nums[j], nums[i - 1]

    # We'll reverse a sequence strating from i to end
    nums[i:] = sorted(nums[i:])

    return nums


print(next_permutation([0, 1, 2, 5, 3, 3, 0]))  # [0, 1, 3, 0, 2, 3, 5]
print(next_permutation([1, 2, 3, 6, 5, 4]))  # [1,2,4,3,5,6]
# print(next_permutation([1,2,3])) # [1,3,2]
# print(next_permutation([3,2,1])) # [1,2,3]
# print(next_permutation([1,1,5])) # [1,5,1]
