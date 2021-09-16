"""
Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.
Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
"""

def make_squares(arr):
    squares = [0 for i in range(len(arr))]
    left = 0
    right = len(arr) - 1
    highest = len(arr) - 1
    while left < right:
        left_sqaure = arr[left] * arr[left]
        right_square = arr[right] * arr[right]
        if left_sqaure > right_square:
            squares[highest] = left_sqaure
            left += 1
        else:
            squares[highest] = right_sqaure
            right -= 1
        highest -= 1
    return squares


if __name__ == '__main__':
    make_squares([-2, -1, 0, 2, 3])

