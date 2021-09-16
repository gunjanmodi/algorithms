def three_way_partition(array, low_value, high_value):
    low = 0
    mid = 0
    high = len(array) - 1
    while mid <= high:
        if array[mid] < low_value:
            array[low], array[mid] = array[mid], array[low]
            low += 1
            mid += 1
        elif array[mid] > high_value:
            array[mid], array[high] = array[high], array[mid]
            high -= 1
        else:
            mid += 1

    print(array)


three_way_partition([12, 9, 1, 3, 8, 6, 7, 2, 5, 14], 3, 7)
