def is_circular_linked_list(head):
    node = head
    node = node.next
    while node and node != head:
        node = node.next
    return node == head
