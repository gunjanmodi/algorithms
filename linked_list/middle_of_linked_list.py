class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == '__main__':
    ll = [23, 8, 67, 134, 29, 45, 1, 77, 32, 9, 12, 89, 101, 19, 53]
    i = 1
    head = Node(ll[0])
    head_copy = head
    while i < len(ll):
        next_node = Node(ll[i])
        head.next = next_node
        head = next_node
        i += 1

    head = head_copy

    head = middle_node(head)

    # Print answer
    while head is not None:
        print(head.data)
        head = head.next
    
    



