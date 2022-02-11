class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.random = None


def copy_random_list(head):
    d = {}
    d[None] = None
    i = 0
    node = head
    while node:
        d[node] = Node(node.val)
        node = node.next
        
    node = head
    while node:
        d[node].next = d[node.next]
        d[node].random = d[node.random]
        node = node.next
    return d[head]