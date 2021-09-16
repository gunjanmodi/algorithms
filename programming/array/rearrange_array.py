def arrange(arr, n):
    for i in range(len(arr)):
        num = arr[i]
        arr[i], arr[num] = arr[num], arr[i]
    return arr


print(arrange([4, 0, 2, 1, 3], 5))