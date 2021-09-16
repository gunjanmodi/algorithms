def get_inversion_count(arr):
    if len(arr) == 1:
        return 0
    # auxiliary_array = arr[:]
    inversion_count = 0
    return _divide_array(arr, 0, len(arr) - 1, inversion_count)


def _divide_array(array, start_idx, end_idx, inversion_count):
    if start_idx == end_idx:
        return
    mid_idx = (start_idx + end_idx ) // 2
    left_half = array[:mid_idx]
    right_half = array[mid_idx:]
    _merge(left_half, right_half, inversion_count)

def _merge(left_half, right_half, inversion_count):
    sorted_array = [None] * len(left_half) + len(right_half)
    k = i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            sorted_array[k] = left_half[i]
            inversion_count += 1
            i += 1
        else:
            sorted_array[k] = right_half[j]
            j += 1
    while i < len(left_half):
        # sorted_array.append(left_half[i])
        i += 1
    while j < len(right_half):
        # sorted_array.append(right_half[j])
        j += 1
    return sorted_array, inversion_count










# print(get_inversion_count([1, 2, 3, 4, 5]))
# print(get_inversion_count([2, 4, 1, 3, 5]))  # 1, 2, 4, 3, 5
print(get_inversion_count([5, 4, 3, 2, 1]))

