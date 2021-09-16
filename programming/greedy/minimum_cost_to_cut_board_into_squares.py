"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(horizontal, vertical):
    horizontal.sort(reverse=True)
    vertical.sort(reverse=True)
    h, v = 0, 0
    horizontal_pieces, vertical_pieces = 1, 1
    total_cost = 0
    while h < len(horizontal) and v < len(vertical):
        if horizontal[h] > vertical[v]:
            total_cost += horizontal[h] * vertical_pieces
            horizontal_pieces += 1
            h += 1
        else:
            total_cost += vertical[v] * horizontal_pieces
            vertical_pieces += 1
            v += 1
    total = 0
    while h < len(horizontal):
        total += horizontal[h]
        h += 1
    total_cost += total * vertical_pieces

    total = 0
    while v < len(vertical):
        total += vertical[v]
        v += 1
    total_cost += total * horizontal_pieces
    return total_cost


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([4, 1, 2], [2, 1, 3, 1, 4]))