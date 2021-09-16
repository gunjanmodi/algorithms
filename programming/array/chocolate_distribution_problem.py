def find_min_diff(arr, m):
    arr.sort()
    # if there are no chocolates or number
    # of students is 0
    if (m == 0 or len(arr) == 0):
        return 0

    # Sort the given packets
    arr.sort()

    # Number of students cannot be more than
    # number of packets
    if (len(arr) < m):
        return -1

    # Largest number of chocolates
    min_diff = arr[len(arr) - 1] - arr[0]

    # Find the subarray of size m such that
    # difference between last (maximum in case
    # of sorted) and first (minimum in case of
    # sorted) elements of subarray is minimum.
    for i in range(len(arr) - m + 1):
        min_diff = min(min_diff, arr[i + m - 1] - arr[i])

    return min_diff



find_min_diff([3, 4, 1, 9, 56, 7, 9, 12], 5)