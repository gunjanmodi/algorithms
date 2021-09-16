"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def solve(s, h, d, n, count):
    count = toh(s, h, d, n, count)
    return count


def toh(s, h, d, n, count):
    count += 1
    if n == 1:
        print(f'moving rod {n} from {s} to rod{d}')
        return
    toh(s, d, h, n - 1, count)
    print(f'moving rod {n} from {s} to rod{d}')
    toh(h, s, d, n - 1, count)
    return count




# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(solve(1, 2, 3, 3, 0))