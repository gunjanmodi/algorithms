"""
Given the head of a linked list, return the list after sorting it in ascending order.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]: # noqa
        list_length = get_list_length(head)
        if not list_length:
            return head
        return merge_sort_helper(head, list_length)


def merge_sort_helper(head, list_length):
    if list_length == 1:
        return head

    mid = list_length // 2

    node1 = node2 = head
    prev = None
    count = 0

    while count < mid:
        prev = node2
        node2 = node2.next
        count += 1

    prev.next = None

    half1 = merge_sort_helper(node1, mid)
    half2 = merge_sort_helper(node2, list_length - mid)

    return do_merge(half1, half2, mid, list_length - mid)


def do_merge(node1, node2, m, n):
    i = j = 0
    sorted_head = ListNode(-1)
    node = sorted_head

    while node1 and node2 and i < m and j < n:
        if node1.val < node2.val:
            node.next = node1
            node1 = node1.next
            i += 1
        else:
            node.next = node2
            node2 = node2.next
            j += 1
        node = node.next

    while node1 and i < m:
        node.next = node1
        node1 = node1.next
        node = node.next
        i += 1

    while node2 and j < n:
        node.next = node2
        node2 = node2.next
        node = node.next
        j += 1

    return sorted_head.next


def get_list_length(node):
    list_length = 0
    while node:
        list_length += 1
        node = node.next
    return list_length
