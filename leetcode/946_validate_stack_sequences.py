from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = [pushed[0]]
        i = 1
        j = 0
        n = len(pushed)
        top = -1
        
        while i < n and j < n:
            if len(stack) > 0 and popped[j] == stack[top]:
                stack.pop()
                j += 1
            else:
                stack.append(pushed[i])
                i += 1
                
        while j < n:
            if popped[j] == stack[top]:
                stack.pop()
                j += 1
            else:
                return False
        return True
        

if __name__ == '__main__':
    s = Solution()
    print(s.validateStackSequences([4,0,1,2,3], [4,2,3,0,1]))
    print(s.validateStackSequences([2], [2]))
    print(s.validateStackSequences([1,2], [2,1]))
    print(s.validateStackSequences([4,0,1,2,3], [4,2,3,0,1]))
    print(s.validateStackSequences([1,2,3,4,5,6,7], [1,2,5,3,6,7,4]))
    print(s.validateStackSequences([0,6,8,9,1,3,2,5,4,7], [6,0,4,9,1,2,3,7,8,5]))
