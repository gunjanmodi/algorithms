def merge_sort(array):
    return merge_sort_helper(array)


def merge_sort_helper(array):
    if len(array) == 1:
        return array

    mid = len(array) // 2
    half1 = merge_sort_helper(array[:mid])
    half2 = merge_sort_helper(array[mid:])
    return do_merge(array, half1, half2)


def do_merge(array, half1, half2):
    sorted_array = []
    i, j = 0, 0

    while i < len(half1) and j < len(half2):
        if half1[i] < half2[j]:
            sorted_array.append(half1[i])
            i += 1
        else:
            sorted_array.append(half2[j])
            j += 1

    while i < len(half1):
        sorted_array.append(half1[i])
        i += 1
    
    while j < len(half2):
        sorted_array.append(half2[j])
        j += 1

    return sorted_array
