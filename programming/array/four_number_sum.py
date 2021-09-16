"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(array, target):
    result = []
    pairs_dict = {}
    for i in range(1, len(array)):
        for j in range(i+1, len(array)):
            current_sum = array[i] + array[j]
            difference = target - current_sum
            if difference in pairs_dict:
                for pair in pairs_dict[difference]:
                    quadruple = pair+[array[i], array[j]]
                    quadruple.sort()
                    result.append(quadruple)

        for k in range(0, i):
            current_sum = array[i] + array[k]
            if current_sum not in pairs_dict:
                pairs_dict[current_sum] = [[array[i], array[k]]]
            else:
                pairs_dict[current_sum].append([array[i], array[k]])
    result.sort()
    return result


def main2(arr, X):
    result = []
    mp = {}
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            mp[arr[i] + arr[j]] = [i, j]

    # Traverse through all pairs and search
    # for X - (current pair summ).
    for i in range(n - 1):
        for j in range(i + 1, n):
            summ = arr[i] + arr[j]

            # If X - summ is present in hash table,
            if (X - summ) in mp:

                # Making sure that all elements are
                # distinct array elements and an element
                # is not considered more than once.
                p = mp[X - summ]
                if (p[0] != i and p[0] != j and p[1] != i and p[1] != j):
                    quadruple = [arr[p[0]], arr[p[1]], arr[i], arr[j]]
                    quadruple.sort()
                    result.append(quadruple)
    result.sort()
    return result





# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([88, 84, 3, 51, 54, 99, 32, 60, 76, 68, 39, 12, 26, 86, 94, 39, 95, 70, 34, 78, 67, 1, 97, 2, 17, 92, 52], 179))
# print(main([7, 6, 4, -1, 1, 2], 16))