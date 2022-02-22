def first_and_last_occurance(array, target):
    start = 0
    end = len(array) - 1
    first_occurance = -1
    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] == target:
            first_occurance = mid
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1 
        else:
            end = mid - 1

    start = 0
    end = len(array) - 1
    last_occurance = -1
    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] == target:
            last_occurance = mid
            start = mid + 1
        elif array[mid] < target:
            start = mid + 1 
        else:
            end = mid - 1
    
    return [first_occurance, last_occurance]


print(first_and_last_occurance([1, 3, 5, 5, 5, 5, 67, 123, 125], 5))