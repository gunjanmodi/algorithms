"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""

from collections import Counter
# Time: O() | Space: O()
# def main(string):
    # counters = Counter(string)
    # left = 0
    # for i in range(len(string)):
    #     character = string[i]
    #
    #     if counters[character] - 1 != 0:
    #         left += 1
    #         counters[character] -= 1
    #     else:
    #         break
    # right = len(string) - 1
    # for j in reversed(range(left, len(string))):
    #     character = string[j]
    #     if counters[character] - 1 != 0:
    #         counters[character] -= 1
    #         right -= 1
    #     else:
    #         break
    # return right - left + 1

from collections import defaultdict

MAX_CHARS = 256
def main(strr):
    n = len(strr)

    # if string is empty or having one char
    if n <= 1:
        return strr

    # Count all distinct characters.
    dist_count = len(set([x for x in strr]))

    curr_count = defaultdict(lambda: 0)
    count = 0
    start = 0
    min_len = n

    # Now follow the algorithm discussed in below
    # post. We basically maintain a window of characters
    # that contains all characters of given string.
    for j in range(n):
        curr_count[strr[j]] += 1

        # If any distinct character matched,
        # then increment count
        if curr_count[strr[j]] == 1:
            count += 1

        # Try to minimize the window i.e., check if
        # any character is occurring more no. of times
        # than its occurrence in pattern, if yes
        # then remove it from starting and also remove
        # the useless characters.
        if count == dist_count:
            while curr_count[strr[start]] > 1:
                if curr_count[strr[start]] > 1:
                    curr_count[strr[start]] -= 1

                start += 1

            # Update window size
            len_window = j - start + 1

            if min_len > len_window:
                min_len = len_window
                start_index = start

    # Return substring starting from start_index
    # and length min_len """
    return len(str(strr[start_index: start_index +
                                     min_len]))




# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long

print(main("AABBBCBBAC"))
print(main("aabcbcdbca"))
print(main("CCCbAbbBbbC"))

print(main("aaab"))
print(main("GEEKSGEEKSFOR"))
print(main("B"))
print(main("CCABBAbBCABB"))
