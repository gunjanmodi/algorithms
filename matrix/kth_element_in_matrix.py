def kth_smallest(matrix, k):
    if not matrix:
        return
    row_indices = [0 for _ in matrix]
    result = None
    i = 0

    while i < k:
        result = get_current_min(matrix, row_indices)
        i += 1
    return result


def get_current_min(matrix, row_indices):
    current_min = float('inf')
    current_min_index = None
    for i, row in enumerate(matrix):
        row_indice = row_indices[i]
        if row_indice == len(row):
            continue
        min_value_at_row = row[row_indice]
        if min_value_at_row < current_min:
            current_min = min_value_at_row
            current_min_index = i

    row_indices[current_min_index] += 1

    return current_min


# print(kth_smallest([ [16, 28, 60, 64], [22, 41, 63, 91], [27, 50, 87, 93], [36, 78, 87, 94]], 4, 3))
# print(kth_smallest([ [10, 20, 30, 40], [15, 25, 35, 45], [24, 29, 37, 48], [32, 33, 39, 50]], 4, 7))
print(kth_smallest([[9, 12, 20, 25, 35], [15, 17, 23, 28, 45], [21, 31, 38, 40, 51], [28, 41, 47, 52, 62], [38, 43, 48, 56, 65]], 23)) # 56
print(kth_smallest([[-5]], 1))
print(kth_smallest([], 1))




