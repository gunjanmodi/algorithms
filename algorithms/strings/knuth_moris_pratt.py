def knuthMorrisPrattAlgorithm(haystack, needle):
    if haystack == None or needle == None:
        return -1
    #generate next array, need O(n) time
    i, j, = -1, 0
    m, n = len(haystack), len(needle)
    next = [-1] * n
    while j < n - 1:  
        #needle[k] stands for prefix, neelde[j] stands for postfix
        if i == -1 or needle[i] == needle[j]:   
            i += 1
            j += 1
            next[j] = i
        else:
            i = next[i]
    #check through the haystack using next, need O(m) time
    i = j = 0
    while i < m and j < n:
        if j == -1 or haystack[i] == needle[j]:
            i, j = i + 1, j + 1
        else:
            j = next[j]
    if j == n:
        return True 
        # return i - j # if you want to return the index
    return False


knuthMorrisPrattAlgorithm("hello", "ll")
