class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        opened = closed = 0
        for i, char in enumerate(s):
            if char == "(":
                opened += 1
            elif char == ")":
                if closed >= opened:
                    continue
                else:
                    closed += 1
            stack.append(char)
        
        if opened == closed:
            return ''.join(stack)
        else:
            another_stack = []
            for i in reversed(range(len(stack))):
                char = stack[i]
                if opened > closed and char == '(':
                    opened -= 1
                    continue
                another_stack.append(char)
                
            another_stack.reverse()
            return ''.join(another_stack)

        
if __name__ == '__main__':
    s = Solution()
    print(s.minRemoveToMakeValid("lee(t(c)o)de)"))
    print(s.minRemoveToMakeValid("a)b(c)d"))
    print(s.minRemoveToMakeValid("))(("))
    print(s.minRemoveToMakeValid("())()((("))
    print(s.minRemoveToMakeValid("(a(b(c)d)"))