"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(items, w):
    n = len(items)
    t = [[-1 for _ in range(w + 1)]] * (n + 1)
    knapsack(items, w, n-1, t)
    return t[-1][-1]


def knapsack(items, w,  n, t):
    if n == 0 or w == 0:
        t[n][w] = 0
    if t[n][w] == -1:
        if items[n][1] <= w:
            t[n][w] = max(
                items[n][0] + knapsack(items, w-items[n][1], n - 1, t),
                knapsack(items, w, n - 1, t)
            )
        else:
            t[n][w] = knapsack(items, w, n - 1, t)
    return t[n][w]











# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
items = [
  [1, 2],
  [4, 3],
  [5, 6],
  [6, 7]
]
capacity = 10
print(main(items, capacity))