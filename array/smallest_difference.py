# noqa
from collections import defaultdict

def smallestDifference1(arrayOne, arrayTwo):
    max_one = max(arrayOne)
    max_two = max(arrayTwo)
    pair = [0] * 2

    smallest_difference = max(max_one, max_two)

    for i in arrayOne:
        for j in arrayTwo:
            diff = max(i, j) - min(i, j)
            if diff < smallest_difference:
                smallest_difference = diff
                pair[0] = i
                pair[1] = j

    return pair


def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    smallest_difference = float("inf")
    pair = [0] * 2
    left = 0
    right = 0

    while left < len(arrayOne) and right < len(arrayTwo):
        difference = max(arrayOne[left], arrayTwo[right]) - min(arrayOne[left], arrayTwo[right])
        if difference < smallest_difference:
            smallest_difference = difference
            pair[0] = arrayOne[left]
            pair[1] = arrayTwo[right]

        if arrayOne[left] <= arrayTwo[right]:
            left += 1

        elif arrayOne[left] > arrayTwo[right]:
            right += 1
    return pair




if __name__ == '__main__':
    array1 = [240, 124, 86, 111, 2, 84, 954, 27, 89]
    array2 = [1, 3, 954, 19, 8]
    o = smallestDifference(array1, array2)
    print(o)