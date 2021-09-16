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


def main(string, pattern):
    result = []
    window_size = len(pattern)
    pattern_hash = get_hash(pattern, window_size, 0)
    for i in range(len(string)):
        current_hash = get_hash(string, window_size, i)
        if current_hash == pattern_hash:
            is_matched = compare_strings(string, pattern, i)
            if is_matched:
                result.append(i)
    return result


def compare_strings(string, pattern, pointer):
    i = pointer
    while i < len(string):
        j = 0
        while j < len(pattern):
            if string[i] == pattern[j]:
                i += 1
                j += 1
            else:
                break
        if j == len(pattern):
            return True
        else:
            return False


def get_hash(string, window_size, pointer=0):
    hash_value = 0
    i = pointer
    count = 0
    while i < len(string) and count < window_size:
        hash_value += (ord(string[i]) - 97)
        i += 1
        count += 1
    return hash_value





# Test case 1: Normal or Given input
print(main("batmanandrobinarebat", "bat"))
# Test case 2: Normal or Given input
print(main("AAAAAAAAAAAAAAAAAA", "AAAAA"))
# Test case 3: Empty
print(main("teststring", ""))
# Test case 4: Empty
print(main("", "testpattern"))
# Test case 5: Too long
print(main("thisisssssssssssssssssssssssssssssssssssssssssssssssssthisssswaaaaaaaaaaaaaaaayyyyyyyyyyyyyyllllonnngstring", "this"))
# Test case 7: Normal
print(main("abesdu", "edu"))
# Test case 8: Normal
print(main("GEEKS FOR GEEKS", "GEEK"))
get_