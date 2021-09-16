def max_product_subarray(arr):
    current_max = arr[0]
    current_min = arr[0]
    previous_max = arr[0]
    previous_min = arr[0]

    max_so_far = arr[0]
    for i in range(1, len(arr)):
        current_max = max(arr[i], max(previous_max * arr[i], previous_min * arr[i]))
        current_min = min(arr[i], min(previous_min * arr[i], previous_max * arr[i]))
        previous_max = current_max
        previous_min = current_min
        max_so_far = max(max_so_far, current_max)
    return max_so_far


print(max_product_subarray([6, -3, -10, 0, 2]))

