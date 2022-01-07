def largest_subarray_sum_k(array, k):
    current_sum = 0
    max_size = 0
    i, j = 0, 0
    while j < len(array):
        current_sum += array[j]
        if current_sum < k:
            j += 1
        else:
            if current_sum == k:
                max_size = max(max_size, j - i + 1)
            else:
                while current_sum > k:
                    current_sum -= array[i]
                    i += 1
            j += 1
    return max_size


print(largest_subarray_sum_k([4, 1, 1, 1, 2, 3, 5], 5))
print(largest_subarray_sum_k([10, 5, 2, 7, 1, 9], 15))
print(largest_subarray_sum_k([-1, 2, 3], 6))
print(largest_subarray_sum_k([1, 4, 3, 3, 5, 5], 16))