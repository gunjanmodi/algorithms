def shift_positives_at_the_end(arr):
    pointer = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i], arr[pointer] = arr[pointer], arr[i]
            pointer += 1
    return arr



print(shift_positives_at_the_end([-12, 11, -13, -5, 6, -7, 5, -3, -6]))
print(shift_positives_at_the_end([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]))
