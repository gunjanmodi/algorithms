"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""

"""
Given an array arr[] of integers and an integer sum,
the task is to count all subsets of the given array with a sum equal to a given sum.
"""

# Time: O() | Space: O()
def main(array, target):
    t = []
    n = len(array)
    for i in range(n + 1):
        t.append([False for _ in range(target + 1)])
    
    for i in range(n + 1):
        for j in range(target + 1):
            if i == 0:
                t[0][j  ] = False
            if j == 0:
                t[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if array[i - 1] <= j:
                t[i][j] = t[i-1][j-array[i - 1]] or t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]

    return t[-1][-1]
    
    


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([2,3,5,8,9,10], 10))
print(main([1, 2, 3, 4, 5], 10))
