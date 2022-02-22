"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(n):
    result = []

    def helper(o, c, temp):
        if o == 0 and c == 0:
            result.append(temp)
            return

        if o == c:
            new_temp = temp + "("
            helper(o-1, c, new_temp)
            
        elif o == 0 and c > 0:
            new_temp = temp + ")"
            helper(o, c-1, new_temp)
    
        else:
            new_temp1 = temp + "("
            helper(o-1, c, new_temp1)

            new_temp2 = temp + ")"
            helper(o, c-1, new_temp2)


    helper(n, n, "")
    return result


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main(3))
