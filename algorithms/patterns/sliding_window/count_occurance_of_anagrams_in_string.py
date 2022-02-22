def count_occurance_of_anagrams(text, pattern):
    ref = {}
    
    result = 0
    for c in pattern:
        ref[c] = ref.get(c, 0) + 1
    required_chars = len(ref)
    
    i = 0
    j = 0
    while j < len(text):
        token = text[j]
        if token in ref :
            ref[token] -= 1
            if ref[token] == 0:
                required_chars -= 1
        
        if j - i + 1 == len(pattern):
            if required_chars == 0:
                result += 1

            win_start = text[i]
            if win_start in ref:
                ref[win_start] += 1
                if ref[win_start] == 1:
                    required_chars += 1
            i += 1
        j += 1
        
    return result

print(count_occurance_of_anagrams("forxxorfxdofr", "for"))
print(count_occurance_of_anagrams("cbaebabacd", "abc"))
print(count_occurance_of_anagrams("aabaabaa", "aaba"))