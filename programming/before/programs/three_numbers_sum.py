def threeNumberSum1(array, targetSum):
    array.sort()
    pairs = []
    for i in array:
        for j in array:
            for k in array:
                if i + j + k == targetSum and i < j and j < k:
                    pairs.append([i,j,k])
    return pairs


def threeNumberSum2(array, targetSum):
    array.sort()
    pairs = []
    for i in array:
        for j in array:
            reminder = targetSum - (i + j)
            if reminder in array and i < j and j < reminder:
                pairs.append([i, j, reminder])

    return pairs


def threeNumberSum3(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array)-1):
        left = i+1
        right = len(array) - 1
        while left < right:
            current_sum = array[i] + array[left] + array[right]

            if current_sum == targetSum:
                triplets.append([array[i], array[left] , array[right]])
                left += 1
                right -= 1

            if current_sum > targetSum:
                right -= 1

            if current_sum < targetSum:
                left += 1

    return triplets

    

if __name__ == '__main__':
    # threeNumberSum1([12 ,3, 1, 2, -6, 5, -8, 6], 0)
    # threeNumberSum2([12 ,3, 1, 2, -6, 5, -8, 6], 0)
    threeNumberSum3([12 ,3, 1, 2, -6, 5, -8, 6], 0)
