class Solution:
    def isValid(self, s: str) -> bool:
        opening_brackets = set(['(','{','['])
        closing_brackets = set([')','}',']'])
        pairs = {")":"(", "}": "{", "]":"["}
        stack = []
        for token in s:
            if token in opening_brackets:
                stack.append(token)
            elif token in closing_brackets and stack:
                if pairs[token] != stack[-1]:
                    return False
                else:
                    stack.pop()
            elif not stack:
                return False
        if len(stack) != 0:
            return False
        return True