"""
Count More than n/k Occurences
Given an array arr[] of size N and an element k.
The task is to find all elements in array that appear more than n/k times.
arr[] = {3,1,2,2,1,2,3,3}
k = 4
Output: 2
"""
from collections import Counter


def count_occurance(arr, k):
    n = len(arr)
    measure = n // k

    counters = Counter(arr)

    occurance = 0
    for key, value in counters.items():
        if value > measure:
            occurance += 1
    return occurance


count_occurance([3,1,2,2,1,2,3,3], 4)

