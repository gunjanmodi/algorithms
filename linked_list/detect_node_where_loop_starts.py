class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def detect_cycle(head):    
    if head is None or head.next is None:
        return
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return
    
    slow = head
    while slow and fast and slow != fast:
        slow = slow.next
        fast = fast.next
    return slow