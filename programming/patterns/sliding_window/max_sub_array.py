def max_sub_array_of_size_k(k, array):
    window_start = 0
    current_sum = 0
    current_max = 0
    for window_end in range(len(array)):
        current_sum += array[window_end]
        if window_end >= k-1:
            current_max = max(current_max, current_sum)
            current_sum -= array[window_start]
            window_start += 1
    return current_max


output = max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])
print(output)