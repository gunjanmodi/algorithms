def get_pairs(arr, n, k):
    count = 0
    matches = {}
    pairs = []
    visited = {}
    for i in range(len(arr)):
        num = arr[i]
        if num not in visited:
            reminder = k - num
            if reminder in matches:
                count += 1
                pairs.append([num, reminder])
            else:
                matches[num] = True
    print(pairs)

    other_pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == k:
                other_pairs.append([arr[i], arr[j]])
    print(other_pairs)
    return count


# array = [48, 24, 99, 51, 33, 39, 29, 83, 74, 72, 22, 46, 40, 51, 67, 37, 78, 76, 26, 28, 76,
#          25, 10, 65, 64, 47, 34, 88, 26, 49, 86, 73, 73, 36, 75, 5, 26, 4, 39, 99, 27, 12, 97,
#          67, 63, 15, 3, 92, 90]
# print(get_pairs(array, len(array), 50))
#
# array = [1, 5, 7, -1, 5]
# get_pairs(array, len(array), 6)

array = [9, 7, 53, 41, 4, 97, 75, 30, 54, 61, 9, 8, 14, 50, 95, 38, 12, 38, 44, 2, 78, 71, 97, 67, 10, 4, 68, 43, 47,
         56, 35, 7, 62, 39, 47, 17, 36, 21, 46, 41, 34, 7]
print(get_pairs(array, len(array), 43))