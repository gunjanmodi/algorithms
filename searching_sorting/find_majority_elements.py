"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""

def majority_element1(nums):
        nums.sort()
        return nums[len(nums)//2]
    
def majority_element2(nums):
    m = {}
    for n in nums:
        m[n] = m.get(n, 0) + 1
        if m[n] > len(nums)//2:
            return n
            
def majority_element(nums):
    candidate, count = nums[0], 0
    for num in nums:
        if num == candidate:
            count += 1
        elif count == 0:
            candidate, count = num, 1
        else:
            count -= 1
    return candidate


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(majority_element([3, 1, 3, 3, 2]))
print(majority_element([1, 2, 3]))