def smallest_subarray_bruteforce(array, x):
    min_length = float('inf')
    for i in range(len(array)):
        current_sum = array[i]
        current_length = 1
        for j in range(i + 1, len(array)):
            current_sum += array[j]
            current_length += 1
            if current_sum > x and current_length < min_length:
                min_length = current_length
    return min_length


def smallest_subarray_sliding_window(array, target):
    window_start, window_end = 0, 0
    current_sum = 0
    min_size = float('inf')
    while window_end < len(array):
        current_sum += array[window_end]
        while current_sum >= target:
            current_sum -= array[window_start]
            min_size = min(min_size, window_end - window_start + 1)
            window_start += 1 
        window_end += 1
    return min_size if min_size !=float('inf') else 0