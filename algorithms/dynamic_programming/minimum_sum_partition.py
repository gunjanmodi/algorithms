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
    array.sort()
    target = sum(array)
    last_row = subset_sum(array, target)
    minimum_sum = float('inf')
    for i in range(target // 2, -1, -1):
        # if last_row[i]:
        minimum_sum = target - (2 * array[i])
    return minimum_sum



def subset_sum(array, target):
    n = len(array)
    t = []
    for i in range(n + 1):
        t.append([False for _ in range(target + 1)])
    for i in range(n + 1):
        for j in range(target + 1):
            if i == 0:
                t[0][j] = False
            if j == 0:
                t[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if array[i - 1] <= j:
                t[i][j] = t[i - 1][j] or t[i - 1][j - array[i - 1]]
            else:
                t[i][j] = t[i - 1][j]
    return t[-1]


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([1, 2, 7])) # 4 
print(main([1, 6, 11, 5])) # 1
print(main([3, 1, 4, 2, 2, 1])) # 1
print(main([5, 6, 6, 5, 7, 4, 7, 6])) # 0
 
