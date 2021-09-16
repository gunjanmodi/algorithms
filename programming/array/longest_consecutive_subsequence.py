def find_longest_consecutive_subsequence(arr):
    if not len(arr):
        return 0
    arr.sort()

    new_arr = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i - 1] != arr[i]:
            new_arr.append(arr[i])

    previous = new_arr[0]
    current_range = [0, 0]
    max_range = [0, 0]
    i = 1
    p = 0
    while i < len(new_arr):
        current = new_arr[i]
        if current - previous <= 1:
            q = i
            current_range[0] = p
            current_range[1] = q
        else:
            if (current_range[1] - current_range[0]) > (max_range[1] - max_range[0]):
                max_range = current_range
            p = i
            current_range = [p, p]
        previous = current
        i += 1
    if (current_range[1] - current_range[0]) > (max_range[1] - max_range[0]):
        max_range = current_range
    return max_range[1] - max_range[0] + 1


def find_longest_consecutive_subsequence_hashing(arr):
    s = set()
    ans = 0

    # Hash all the array elements
    for ele in arr:
        s.add(ele)

    # check each possible sequence from the start
    # then update optimal length
    for i in range(len(arr)):

        # if current element is the starting
        # element of a sequence
        if (arr[i] - 1) not in s:

            # Then check for next elements in the
            # sequence
            j = arr[i]
            while (j in s):
                j += 1

            # update  optimal length if this length
            # is more
            ans = max(ans, j - arr[i])
    return ans


print(find_longest_consecutive_subsequence([2, 6, 1, 9, 4, 5, 3]))
print(find_longest_consecutive_subsequence([2, 6, 1, 9, 4, 5]))
print(find_longest_consecutive_subsequence([1, 2, 3]))
print(find_longest_consecutive_subsequence([]))
print(find_longest_consecutive_subsequence([1, 9, 3, 10, 4, 20, 2]))
print(find_longest_consecutive_subsequence([9, 8, 7, 6, 5, 4, 9, 8, 7, 6, 5, 4, 4]))
