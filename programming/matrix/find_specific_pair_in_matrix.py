def find_pair(matrix):
    n = len(matrix)
    max_value = 0
    # for a in range(n - 1):
    #     for b in range(n - 1):
    #         for d in range(a + 1, n):
    #             for e in range(b + 1, n):
    #                 value1 = matrix[a][b]
    #                 value2 = matrix[d][e]
    #                 if max_value < int(value2 - value1):
    #                     max_value = int(value2 - value1)
    return max_value


print(find_pair([[1, 2, -1, -4, -20], [-8, -3, 4, 2, 1], [3, 8, 6, 1, 3], [-4, -1, 1, 7, -6 ], [0, -4, 10, -5, 1]]))
