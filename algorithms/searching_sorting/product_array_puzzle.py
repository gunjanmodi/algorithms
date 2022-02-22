"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""
# Time: O(n) | Space: O(n)
def productExceptSelf(array):
    n = len(array)
    output1 = [1] * n
    current_product = 1
    for i in range(n):
        output1[i] = current_product
        current_product = current_product * array[i]

    output2 = [1] * n
    current_product = 1
    for i in reversed(range(n)):
        output2[i] = current_product
        current_product = current_product * array[i]
    
    for i in range(n):
        array[i] = output1[i] * output2[i]
    return array


def productExceptSelf2(array):
    output = []
    p = 1
    for i in range(len(array)):
        output.append(p)
        p = p * array[i]

    p = 1
    for i in range(len(array) - 1, -1, -1):
        output[i] = output[i] * p
        p = p * array[i]
    return output


print(productExceptSelf([1, 0]))
print(productExceptSelf([1, 0]))