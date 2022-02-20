def min_window_substring(s, t):
    d = {}
    for c in t:
        d[c] = d.get(c, 0) + 1
    counter = len(d)
    min_window = float('inf')
    i, j, head = 0, 0, 0
    while j < len(s):
        token = s[j]
        if token in d:
            d[token] -= 1
            if d[token] == 0:
                counter -= 1

        while counter == 0:
            if j - i + 1 < min_window:
                min_window = j - i + 1
                head = i
            if s[i] in d:
                d[s[i]] += 1
                if d[s[i]] > 0:
                    counter += 1
            i += 1
        j += 1
        
    if min_window == float('inf'):
        return ""
    
    return s[head:head+min_window]

print(min_window_substring("TOTMTAPTAT", "TTA"))
print(min_window_substring("ADOBECODEBANC", "ABC"))
print(min_window_substring("a", "a"))
print(min_window_substring("a", "aa"))