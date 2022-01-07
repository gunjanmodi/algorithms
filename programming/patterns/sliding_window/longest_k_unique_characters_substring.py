def longest_substring_k_unique_characters(string, k):
    i, j =0, 0
    d = {}
    max_size = 0
    while j < len(string):
        d[string[j]] = d.get(string[j], 0) + 1
        if len(d.keys()) < k:
            j += 1
        else:
            if len(d.keys()) == k:
                max_size = max(max_size, j - i + 1)
            else:
                while len(d.keys()) > k:
                    d[string[i]] -= 1
                    if d[string[i]] == 0:
                        del d[string[i]]
                    i += 1
            j += 1
    return max_size if max_size > 0 else -1


print(longest_substring_k_unique_characters("aabacbebebe", 3))
print(longest_substring_k_unique_characters("aaaa", 2))