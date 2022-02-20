def get_min_diff(arr, k):
    min_so_far = float("inf")
    max_so_far = float("-inf")
    i = 0
    while i < len(arr):
        if arr[i] - k < 0:
            arr[i] += k
        else:
            arr[i] -= k
        min_so_far = min(min_so_far, arr[i])
        max_so_far = max(max_so_far, arr[i])
        i += 1

    return max_so_far - min_so_far


print(get_min_diff([2, 6, 3, 4, 7, 2, 10, 3, 2, 1], 5))
