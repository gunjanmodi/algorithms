def is_isomorphic(string1, string2):
    # if len(string1) != len(string2):
    #     return False
    reference = {}
    visited = {}
    i = 0
    while i < len(string1):
        reference[i] = [string1[i], string2[i]]
        if string1[i] in visited:
            other = visited[string1[i]]
            if reference[i] != reference[other]:
                return False
        if string2[i] in visited:
            other = visited[string2[i]]
            if reference[i] != reference[other]:
                return False
        visited[string1[i]] = i
        visited[string2[i]] = i
        i += 1
    return True


print(is_isomorphic("exudzhi", "ftakcz"))
print(is_isomorphic("egg", "add"))
print(is_isomorphic("foo", "bar"))
print(is_isomorphic("pijthbsfy", "fvladzpbf"))
