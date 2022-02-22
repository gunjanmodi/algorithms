from collections import defaultdict

def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    n = len(s)
    m1, m2 = defaultdict(str), defaultdict(str)
    for i in range(n):
        if m1[s[i]] != m2[t[i]]:
            return False
        m1[s[i]] = i + 1
        m2[t[i]] = i + 1
    return True


print(is_isomorphic("exudzhi", "ftakcz"))
print(is_isomorphic("egg", "add"))
print(is_isomorphic("foo", "bar"))
print(is_isomorphic("pijthbsfy", "fvladzpbf"))
