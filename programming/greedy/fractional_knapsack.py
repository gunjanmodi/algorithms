"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(weights, values, capacity):
    mapping = list(zip(weights, values))
    mapping.sort(key=lambda x: -x[1]/x[0])
    result, applied_count, i = 0, 0, 0
    weight, value = 0, 1
    while i < len(mapping):
        if capacity >= mapping[i][weight]:
            capacity -= mapping[i][weight]
            result += mapping[i][value]
            applied_count += 1
        else:
            result += mapping[i][value] * capacity / mapping[i][weight]
            break
        i += 1
    return result


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([10, 40, 20, 30], [60, 40, 100, 120], 50)) # 240
print(main([10, 20], [60, 100], 50)) # 160
print(main([50, 20, 30], [600, 500, 400], 70)) # 1140
print(main([10, 5, 20], [200, 50, 100], 15)) # 250
print(main([10, 20, 30], [60, 100, 120], 50)) # 240

