def binary_search(arr, key):
#   arr.sort()
  left = 0
  right = len(arr) - 1
  is_ascending = arr[left] < arr[right]
  while left <= right:
    middle = (left + right) // 2
    if key == arr[middle]:
      return middle

    if is_ascending:
        if key > arr[middle]:
            left = middle + 1
        else:
            right = middle - 1
    else:
        if key > arr[middle]:
            right = middle - 1
        else:
            left = middle + 1
  return -1

def main():
  print(binary_search([4, 6, 10], 10))
  print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
  print(binary_search([10, 6, 4, 2, 1], 10))
  print(binary_search([10, 6, 4], 4))


main()
