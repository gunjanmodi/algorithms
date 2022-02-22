"""
Link: https://leetcode.com/problems/excel-sheet-column-number/
Given a string columnTitle that represents the column title as appear in an Excel sheet,
return its corresponding column number.
"""


class Solution: # noqa
    def titleToNumber(self, columnTitle: str) -> int:  # noqa
        n = len(columnTitle) # noqa
        if not columnTitle:
            return 0
        answer = []
        x = len(columnTitle) - 1
        for i in range(n):
            current = columnTitle[i]
            position = pos(current)
            answer.append(position * pow(26, x))
            x -= 1
        return sum(answer)


def pos(char):
    return ord(char) - 64

