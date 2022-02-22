def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)
    return array

def quick_sort_helper(array, start, end):
    if start >= end:
        return
    
    pivot = array[start]
    left = start
    right = end

    while left <= right:
        while left <= right and array[left] < pivot:
            left += 1
        while left <= right and array[right] > pivot:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    quick_sort_helper(array, start, right - 1)
    quick_sort_helper(array, left, end)





if __name__ == '__main__':
    ans = quick_sort([10, 16, 8, 12,  15, 6, 3, 9, 5])
    print(ans)
    
