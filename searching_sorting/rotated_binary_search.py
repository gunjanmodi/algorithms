def rotated_binary_search(array, target):
    min_index = find_min_index(array)
    if min_index == 0:
        return binary_search(array, 0, len(array) - 1, target)
    elif array[0] <= target <= array[min_index - 1]: 
        return binary_search(array, 0, min_index - 1, target)
    else:
        return binary_search(array, min_index, len(array) - 1, target)


def binary_search(array, left, right, target):
    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid
        
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def find_min_index(array):
    left = 0
    right = len(array) - 1
    n = len(array)

    min_index = -1

    while left <= right:
        if array[left] < array[right]:
            return left
        mid = (left + right) // 2

        next = (mid + 1) % n
        prev = (mid - 1 + n) % n

        if array[mid] <= array[prev] and array[mid] <= array[next]:
            return mid
        elif array[left] <= array[mid]:
            left = mid + 1
        elif array[right] >= array[mid]:
            right = mid - 1

    return min_index


print(rotated_binary_search([0, 1, 21, 33, 37, 45, 61, 71, 72, 73], 0))
print(rotated_binary_search([45, 61, 71, 72, 73, 0, 1, 21, 33, 37], 33))
print(rotated_binary_search([5, 1, 2, 3, 4], 3))
print(rotated_binary_search([1, 2, 3, 4, 5], 6))
print(rotated_binary_search([11, 12, 15, 18, 2, 5, 6, 8], 18))