"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(prices, k):
    mapping = []
    for i, price in enumerate(prices):
        mapping.append((i+1, price))
    mapping.sort(key=lambda x: x[1])
    total_qty = 0
    for i in range(len(mapping)):
        qty = min(mapping[i][0], k // mapping[i][1])
        k -= mapping[i][1] * qty
        total_qty += qty
    return total_qty




# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([10, 7, 19], 45))