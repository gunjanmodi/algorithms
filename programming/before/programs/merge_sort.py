def merge_sort1(array):
    if len(array) == 1:
        return array

    middle_index = len(array) // 2
    left_half = merge_sort(array[:middle_index])
    right_half = merge_sort(array[middle_index:])
    return merge_sorted_array(left_half, right_half)

def merge_sorted_array(left_half, right_half):
    sorted_array = [None] * (len(left_half) + len(right_half))
    k = i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            sorted_array[k] = left_half[i]
            i += 1
        else:
            sorted_array[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        sorted_array[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        sorted_array[k] = right_half[j]
        j += 1
        k += 1

    return sorted_array


def merge_sort(array):
    if len(array) <= 1:
        return array

    auxiliary_array = array[:]
    merge_sort_helper(array, 0, len(array) - 1, auxiliary_array)
    return array

def merge_sort_helper(main_array, start_index, end_index, auxiliary_array):
    if start_index == end_index:
        return
    middle_index = (start_index + end_index) // 2
    merge_sort_helper(auxiliary_array, start_index, middle_index, main_array)
    merge_sort_helper(auxiliary_array, middle_index + 1, end_index, main_array)
    do_merge(main_array, start_index, middle_index, end_index, auxiliary_array)

def do_merge(main_array, start_index, middle_index, end_index, auxiliary_array):
    # print(main_array, start_index, middle_index, end_index, auxiliary_array)
    k = start_index
    i = start_index
    j = middle_index + 1
    while i <= middle_index and j <= end_index:
        if auxiliary_array[i] <= auxiliary_array[j]:
            main_array[k] = auxiliary_array[i]
            i += 1
        else:
            main_array[k] = auxiliary_array[j]
            j += 1
        k += 1

    while i <= middle_index:
        main_array[k] = auxiliary_array[i]
        i += 1
        k += 1

    while j <= end_index:
        main_array[k] = auxiliary_array[j]
        j += 1
        k += 1





if __name__ == '__main__':
    print(merge_sort([8, 5, 2, 9, 5, 6, 3]))