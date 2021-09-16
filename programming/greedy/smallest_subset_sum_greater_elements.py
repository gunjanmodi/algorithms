"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(arr):
    # calculating HALF of array sum
    # halfSum = 0
    # for i in range(len(arr)):
    #     halfSum = halfSum + arr[i]

    # halfSum = int(halfSum / 2)

    # sort the array in descending order.
    arr.sort(reverse=True)

    res = 0

    before_sum = sum(arr)
    curr_sum = 0
    for i in range(len(arr)):

        curr_sum += arr[i]
        before_sum -= arr[i]
        res += 1

        # current sum greater than sum
        if curr_sum > before_sum:
            return res

    return res


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([3, 1, 7, 1]))
print(main([2, 1, 2]))