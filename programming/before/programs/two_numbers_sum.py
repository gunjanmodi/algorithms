def twoNumberSum(array, targetSum):
    pairs = []
    for i in array:
        for j in array:
            if i + j == targetSum and i != j:
                pairs.append((i,j))
    if len(pairs) > 0:
        return pairs[0]
    return pairs


def twoNumberSum1(array, targetSum):
    for i in array:
        for j in array:
            if i + j == targetSum and i != j:
                return [i, j]
    return []


def twoNumberSum2(array, targetSum):
    pairs = {}
    for i in array:
        reminder = targetSum - i
        if reminder in array:
            return [i, reminder]
        else:
            pairs[i] = True
    return []

def twoNumberSum3(array, targetSum):
    array.sort()
    print(array)
    left = 0
    right = len(array) - 1
    while left < right:
        current_sum = array[left] + array[right]
        print("-----------")
        print(array[left])
        print(array[right])
        print(current_sum)
        if current_sum == targetSum:
            return [array[left], array[right]]
        if current_sum < targetSum:
            left += 1
        if current_sum > targetSum:
            right -= 1

        

if __name__ == '__main__':
    o = twoNumberSum([3,5,-4,8,11,1,-1,6],10)
    print(o)