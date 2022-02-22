"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(values, weights, capacity):
    n = len(values)
    w = capacity
    
    t = []
    for i in range(n + 1):
        t.append([-1 for _ in range(w+1)])
    
    for i in range(n + 1):
        for j in range(w + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
                
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if wt[i-1] <= j:
                t[i][j] = max(
                    val[i-1] + t[i-1][j-wt[i-1]],
                    t[i-1][j]
                    )
            else:
                t[i][j] = t[i-1][j]
    return t[-1][-1]


def knapsack(values, weights, n, capacity):
    if n == 0 or capacity == 0:
        return 0
    if weights[n] <= capacity:
        return max(values[n] + knapsack(values, weights, n-1, capacity-weights[n]),
                               knapsack(values, weights, n-1, capacity)
                   )
    else:
        return knapsack(values, weights, n-1, capacity)




# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
values = [1, 4, 5, 6]
weights = [2, 3, 6, 7]
capacity = 10
# values = [60,100,120]
# weights = [10,20,30]
# capacity = 50
print(main(values, weights, capacity))