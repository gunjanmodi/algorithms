def find_longest_consecutive_subsequence(array):
    array.sort()
    current_longest = min(1, len(array))
    longest = 0
    for i in range(1, len(array)):
        if array[i - 1] == array[i]:
            continue
        elif array[i - 1] + 1 == array[i]:
            current_longest += 1
        else:
            current_longest = 1
        longest = max(longest, current_longest)

    return max(longest, current_longest)


def find_longest_consecutive_subsequence_hashing(nums):
    longest = 0
    s = set(nums)

    for num in nums:
        current_longest = 1
        j = 1

        while num - j in s:
            s.remove(num - j)
            current_longest += 1
            j += 1

        j = 1
        while num + j in s:
            s.remove(num + j)
            current_longest += 1
            j += 1
        longest = max(longest, current_longest)

    return longest


print(find_longest_consecutive_subsequence([2, 6, 1, 9, 4, 5, 3]))
print(find_longest_consecutive_subsequence([1, 9, 3, 10, 4, 20, 2]))
print(find_longest_consecutive_subsequence([1, 2, 3, 4, 5]))

# print(find_longest_consecutive_subsequence([2, 6, 1, 9, 4, 5]))
# print(find_longest_consecutive_subsequence([1, 2, 3]))
# print(find_longest_consecutive_subsequence([]))
# print(find_longest_consecutive_subsequence([1, 9, 3, 10, 4, 20, 2]))
# print(find_longest_consecutive_subsequence([9, 8, 7, 6, 5, 4, 9, 8, 7, 6, 5, 4, 4]))
