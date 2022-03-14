class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for p in path.split("/"):
            if p == '' or p == '.':
                continue
            elif stack and p == '..':
                stack.pop()
            elif p != '..':
                stack.append(p)
            
        return '/'+'/'.join(stack)


if __name__ == '__main__':
    s = Solution()
    print(s.simplifyPath("/a/./b/../../c/"))
    print(s.simplifyPath("/home//foo/"))
    print(s.simplifyPath("/../"))