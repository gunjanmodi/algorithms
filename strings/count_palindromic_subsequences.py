"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""

# Time: O()
# Space: O()


# def main(string):
#     count = 0
#     for i in range(len(string)):
#         # print(string[i])
#         for j in range(i, len(string)):
#             substring = string[i:j+1]
#             if check_palindrome(substring):
#                 count += 1
#     return count
#
#
# def check_palindrome(string):
#     left = 0
#     right = len(string) - 1
#     while left < right:
#         if string[left] != string[right]:
#             return False
#         else:
#             left += 1
#             right -= 1
#     return True


def main(string):
    cps = []
    for i in range(len(string) + 2):
        row = [0] * (len(string) + 2)
        cps.append(row)

    for i in range(len(string)):
        cps[i][i] = 1
    print(cps)

    # for L in range(2, len(string) + 1):
    #     for i in range(len(string)):
            


def is_palindrome(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True




# Test case 1: Normal or Given input
print(main("abcd"))
# Test case 2: Normal or Given input
# print(main("aab"))
# Test case 3: Normal or Given input
# print(main("abaxyzzyxf"))
# Test case 4: Negative
# print(main())
# Test case 5: Empty
# print(main())
# Test case 6: Too long
# print(main())
# Test case 7
# Test case 8
# Test case 9