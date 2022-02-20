"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(array):
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    if len(array) == 2:
        return max(array[0], array[1])

    dp = [0] * len(array)
    dp[0] = array[0]
    dp[1] = max(array[0], array[1])

    for i in range(2, len(array)):
        dp[i] = max( dp[i-2] + array[i], dp[i-1])
    return dp[-1]





# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([5, 3, 4, 11, 2]))
