class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def reverse_linked_list(head, k):
    previous, current = None, head
    i = 0
    while current is not None and i < k:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
        i += 1
    return previous, current


def reverse_k_group(head, k):
    count, node = 0, head
    while node is not None and count < k:
        node = node.next
        count += 1

    if count < k:
        return head
    
    new_prev, new_current = reverse_linked_list(head, k)
    head.next = reverse_k_group(new_current, k)
    return new_prev

if __name__ == '__main__':
    ll = [1, 2, 2, 4, 5, 6, 7, 8]
    i = 1
    head = Node(ll[0])
    head_copy = head
    while i < len(ll):
        next_node = Node(ll[i])
        head.next = next_node
        head = next_node
        i += 1

    head = head_copy

    head = reverse_k_group(head, 4)

    # Print answer
    while head is not None:
        print(head.data)
        head = head.next
