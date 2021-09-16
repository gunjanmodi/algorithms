from collections import defaultdict

def group_anagram(words):
    anagrams = defaultdict(list)
    for word in words:
        ordered_key = ''.join(sorted(word))
        anagrams[ordered_key].append(word)
    return list(anagrams.values())          

if __name__:
    print(group_anagram(["yo", "act", "flop", "tac", "cat", "oy", "olfp"]))
