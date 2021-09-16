"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(n, k):
    array = [i for i in range(n)]
    k -= 1
    return recursive_helper(array, 0, k)


def recursive_helper(array, previous_alive, k):
    if len(array) == 1:
        return array[-1] + 1
    index_to_kill = (previous_alive + k) % len(array)
    array = array[:index_to_kill] + array[index_to_kill + 1:]
    return recursive_helper(array, index_to_kill, k)


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main(3, 2))
print(main(5, 3))