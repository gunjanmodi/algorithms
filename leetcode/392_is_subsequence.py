class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
                
        if i > len(s) - 1:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isSubsequence("abc", "ahbgdc"))
    print(s.isSubsequence("axc", "ahbgdc"))
    print(s.isSubsequence("axc", "ahbgdc"))
    print(s.isSubsequence("", "abc"))
    print(s.isSubsequence("ace", "abcde"))
