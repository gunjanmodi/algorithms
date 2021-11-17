def find_min_diff(array, m):
    if m > len(array):
        return -1
    if m == 0 or len(array) == 0:
        return 0
    array.sort()
    min_diff = float('inf')
    window_start = 0
    for window_end in range(len(array)):
        if window_end >= m - 1:
            current_diff = array[window_end] - array[window_start]
            min_diff = min(min_diff, current_diff)
            window_start += 1
    return min_diff



print(find_min_diff([3, 4, 1, 9, 56, 7, 9, 12], 5))