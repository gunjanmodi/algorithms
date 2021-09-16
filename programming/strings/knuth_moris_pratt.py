"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""

# Time: O()
# Space: O()


class Solution:
    def main(self, string, substring):
        pattern, current_min, current_max = self.build_pattern(substring)
        return self.search_pattern(string, substring, pattern)

    def search_pattern(self, string, substring, pattern):
        j = 0
        for i in range(len(string)):
            if string[i] == substring[j]:
                if j == len(substring) - 1:
                    return True
                i += 1
                j += 1
            elif j > 0:
                j = pattern[j-1] + 1
            else:
                i += 1
        return False

    def build_pattern(self, substring):
        pattern = [-1 for _ in substring]
        j = 0
        i = 1
        while i < len(substring):
            if substring[i] == substring[j]:
                pattern[i] = j
                i += 1
                j += 1
            elif j > 0:
                j = pattern[j - 1] + 1
            else:
                i += 1
        return pattern


s = Solution()
# Test case 1: Normal or Given input
print(s.main("aefoaefcdaefcdaed", "aefaedaefaefa"))
# Test case 2: Normal or Given input
print(s.main("aefaefaefaedaefaedaefaefa", "aefcdaed"))
# Test case 3: Normal or Given input
# print(s.main())
# Test case 4: Negative
# print(s.main())
# Test case 5: Empty
# print(s.main())
# Test case 6: Too long
# print(s.main())
# Test case 7
# Test case 8
# Test case 9