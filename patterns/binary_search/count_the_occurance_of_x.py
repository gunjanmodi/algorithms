def count_occurance_of_target(array, target):
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
    
    if first_occurance == -1:
        return 0
    
    return last_occurance - first_occurance + 1


print(count_occurance_of_target([1, 3, 5, 5, 5, 5, 67, 123, 125], 5))
print(count_occurance_of_target([1, 3, 5, 5, 5, 5, 67, 123, 125], 56))