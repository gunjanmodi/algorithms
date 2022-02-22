"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(array):
    # count = 0
    # for i in range(len(array)):
    #     size = 1
    #     while size <= len(array)- i:
    #         subarray = [array[i]]
    #         for j in range(i + 1, len(array)):
    #             if len(subarray) < size:
    #                 subarray.append(array[j])
    #             else:
    #                 break
    #         if sum(subarray) == 0:
    #             count += 1
    #         size += 1
    # return count
    count = 0
    sums = 0
    d = dict()
    d[0] = 1
    for i in range(len(array)):
        sums += array[i]
        count += d.get(sums, 0)
        d[sums] = d.get(sums,0) + 1
    return count


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
# print(main([1, 2, 3, 4]))
print(main([6, -1, -3, 4, -2, 2, 4, 6, -12, -7]))
         # [6,  5,  2, 6, 4,  6, 10,16, 4,   -3 ]
