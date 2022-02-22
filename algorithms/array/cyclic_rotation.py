def rotate( arr, n):
    for i in range(len(arr)):
        arr[i], arr[-1] = arr[-1], arr[i]
    return arr

print(rotate([1,2,3,4,5], 5))

