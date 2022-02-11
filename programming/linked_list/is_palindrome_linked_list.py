class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def linked_list_palindrome(head):
    # Find Mid
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second part
    mid = slow
    prev, current = None, mid
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # Compare two parts
    node1, node2 = head, prev
    while  node2:
        if node1.data != node2.data:
            return False
        node1 = node1.next
        node2 = node2.next
    return True