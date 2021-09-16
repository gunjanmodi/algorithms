"""
Given an array arr[] of N non-negative integers representing the height of blocks.
If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season.
"""
def tapping_water(heights):
    if not heights:
        return 0

    total = 0
    left_max = heights[0]

    right_maxes = [0 for _ in heights]
    j = len(heights) - 1
    right_max = heights[j]

    while j >= 0:
        right_maxes[j] = right_max
        right_max = max(heights[j], right_max)
        j -= 1

    i = 1

    while i + 1 < len(heights):
        block = heights[i]
        left_max = max(left_max, block)

        reference = min(left_max, right_maxes[i])
        if not reference < block:
            total += reference - block
        i += 1

    return total


# print(tapping_water([3, 0, 0, 2, 0, 4]))
# print(tapping_water([7, 4, 0, 9]))
# print(tapping_water([8, 8, 2, 4, 5, 5, 1]))
print(tapping_water([0,1,0,2,1,0,1,3,2,1,2,1]))
print(tapping_water([4,2,0,3,2,5]))
