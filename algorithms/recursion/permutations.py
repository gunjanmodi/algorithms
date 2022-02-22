def permutations(nums):
    result = []
    permutations_helper(nums, 0, result)
    return result


def permutations_helper(nums, k, result):
    if k == len(nums) - 1:
        result.append(nums[:])
        return
    for i in range(k, len(nums)):
        swap(nums, k, i)
        permutations_helper(nums, k + 1, result)
        swap(nums, k, i)


def swap(array, a, b):
    array[a], array[b] = array[b], array[a]


print(permutations([1,2,3]))
# print(permutations([1,2]))
# print(permutations([1]))
# print(permutations([]))