def max_sub_array_of_size_k(array, k):
    i = 0
    current_sum = array[0]
    max_sum = array[0]
    for j in range(1, len(array)):
        current_sum += array[j]
        if j - i + 1 >= k:
            max_sum = max(current_sum, max_sum)
            current_sum -= array[i]
            i += 1
    return max_sum


output = max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])
print(output)