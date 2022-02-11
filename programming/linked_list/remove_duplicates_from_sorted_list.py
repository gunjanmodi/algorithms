class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

def remove_duplicates(head):
    node = head
    while node and node.next:
        if node.data == node.next.data:
            node.next = node.next.next
        else:
            node = node.next
    return head


if __name__ == '__main__':
    ll = [1, 1, 2, 2, 3, 4, 4, 5, 6, 6]
    i = 1
    head = Node(ll[0])
    head_copy = head
    while i < len(ll):
        next_node = Node(ll[i])
        head.next = next_node
        head = next_node
        i += 1

    head = head_copy

    head = remove_duplicates(head)

    # Print answer
    while head is not None:
        print(head.data)
        head = head.next
    
    



