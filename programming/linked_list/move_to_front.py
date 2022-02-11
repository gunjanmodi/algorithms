class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def move_to_front(head):
    previous, current = None, head
    while current and current.next:
        previous = current
        current = current.next

    previous.next = None
    current.next = head
    head = current
    return head

if __name__ == '__main__':
    ll = [1, 2, 3, 4, 5]
    i = 1
    head = Node(ll[0])
    head_copy = head
    while i < len(ll):
        next_node = Node(ll[i])
        head.next = next_node
        head = next_node
        i += 1

    head = head_copy

    head = move_to_front(head)

    # Print answer
    while head is not None:
        print(head.data)
        head = head.next
