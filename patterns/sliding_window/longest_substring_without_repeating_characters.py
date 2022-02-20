def longest_substring_without_repeating_characters(string):
    i, j =0, 0
    d = {}
    max_size = 0

    while j < len(string):
        d[string[j]] = d.get(string[j], 0) + 1
        if len(d.keys()) == j - i + 1:
            max_size = max(max_size, j - i + 1)
        elif len(d.keys()) < j - i + 1:
            while len(d.keys()) < j - i + 1:
                d[string[i]] -= 1
                if d[string[i]] == 0:
                    del d[string[i]]
                i += 1
        j += 1
    return max_size if max_size > 0 else -1


def longest_substring_without_repeating_characters_2(s):
        i = maxLength = 0
        usedChar = {}
        
        for j in range(len(s)):
            if s[j] in usedChar and i <= usedChar[s[j]]:
                i = usedChar[s[j]] + 1
            else:
                maxLength = max(maxLength, j - i + 1)

            usedChar[s[j]] = j

        return maxLength


print(longest_substring_without_repeating_characters("abcabcbb"))
print(longest_substring_without_repeating_characters("bbbbb"))
print(longest_substring_without_repeating_characters("pwwkew"))