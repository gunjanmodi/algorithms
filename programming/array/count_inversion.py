def count_inversions(array):
    return subarray_inversion_count(array, 0, len(array) - 1)


def subarray_inversion_count(array, start, end):
    if end <= start:
        return 0
    mid = (start + end) // 2
    left_subarray_inversion_count = subarray_inversion_count(array, start, mid)
    right_subarray_inversion_count = subarray_inversion_count(array, mid + 1, end)
    merged_inversion_count = merge_inversion_count(array, start, mid, end)
    return left_subarray_inversion_count + right_subarray_inversion_count + merged_inversion_count


def merge_inversion_count(array, start, mid, end):
    sorted_temp_array = [0] * len(array)
    i = start
    j = mid + 1
    k = start
    inversion_count = 0

    while i <= mid and j <= end:
        if array[i] <= array[j]:
            sorted_temp_array[k] = array[i]
            i += 1
            k += 1
        else:
            sorted_temp_array[k] = array[j]
            inversion_count += mid + 1 - i
            j += 1
            k += 1

    while i <= mid:
        sorted_temp_array[k] = array[i]
        i += 1
        k += 1

    while j <= end:
        sorted_temp_array[k] = array[j]
        j += 1
        k += 1

    for idx in range(start, end + 1):
        array[idx] = sorted_temp_array[idx]

    return inversion_count


print(count_inversions([2, 3, 3, 1, 9, 5, 6]))
