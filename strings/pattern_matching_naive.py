"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""

# Time: O(S*P) where S is length of string and P is length of the pattern
# Space: O(1)


def main(string, pattern):
    if not string or not pattern:
        return -1
    i = 0
    result = []
    current_start = None
    while i < len(string):
        j = 0
        while j < len(pattern) and i < len(string):
            if pattern[j] == string[i]:
                if current_start is None:
                    current_start = i
                j += 1
                i += 1
            else:
                i += 1
                current_start = None
                break
        if j == len(pattern):
            result.append(current_start+1)
            current_start = None
    return result if len(result) > 0 else -1


# Test case 1: Normal or Given input
print(main("batmanandrobinarebat", "bat"))
# Test case 2: Normal or Given input
print(main("AAAAAAAAAAAAAAAAAA", "AAAAA"))
# Test case 3: Normal or Given input
print(main("teststring", ""))
# Test case 4: Negative
print(main("", "testpattern"))
# Test case 5: Empty
print(main("thisisssssssssssssssssssssssssssssssssssssssssssssssssthisssswaaaaaaaaaaaaaaaayyyyyyyyyyyyyyllllonnngstring", "this"))
# Test case 6: Too long
print(main("AAAAAAAAAAAAAAAAAA", "AAAAA"))
# Test case 7
print(main("abesdu", "edu"))
# Test case 8
# Test case 9