"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(items, capacity):
    n = len(items)
    return knapsack(items, capacity, n - 1)


def knapsack(items, capacity, n):
    if n == 0 or capacity == 0:
        return 0

    if items[n][1] <= capacity:
        return max(
            items[n][0] + knapsack(items, capacity - items[n][1], n - 1),
            knapsack(items, capacity, n - 1)
        )
    else:
        return knapsack(items, capacity, n - 1)


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
items = [
  [1, 2],
  [4, 3],
  [5, 6],
  [6, 7]
]
capacity = 10
print(main(items, capacity))