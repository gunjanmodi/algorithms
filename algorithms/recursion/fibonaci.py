"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def get_nth_fib(n):
    last_two= [0, 1]
    counter = 3

    while counter <= n:
        next_fib = last_two[0] + last_two[1]
        last_two[0] = last_two[1]
        last_two[1] = next_fib
        counter += 1
    return last_two[1] if n > 1 else last_two[0]


def getNnthFib(n):
    if n == 2:
        return 1
    if n == 1:
        return 0
    return getNnthFib(n - 1) + getNnthFib(n - 2)

# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(get_nth_fib(6))
print(getNnthFib(6))