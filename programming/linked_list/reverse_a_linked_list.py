class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def reverse_singly_linked_list(head):
    previous, current = None, head
    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous


def reverse_doubly_linked_list(head):
    previous, current = None, head
    while current is not None:
        next_node = current.next
        current.next = previous
        current.prev = next_node
        previous = current
        current = next_node
    return previous


if __name__ == '__main__':
    ll = [1, 2, 3, 4, 5, 6, 7, 8]
    i = 1
    head = Node(ll[0])
    head_copy = head
    while i < len(ll):
        next_node = Node(ll[i])
        head.next = next_node
        head = next_node
        i += 1

    head = head_copy

    head = reverse_singly_linked_list(head)

    # Print answer
    while head is not None:
        print(head.data)
        head = head.next
