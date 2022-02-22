class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

def remove_duplicates(head):
    current = previous = head
    visited = set()
    while current is not None:
        if current.data in visited:
            previous.next = current.next
            current.next = None
            current = previous.next
        else:
            visited.add(current.data)
            previous = current
            current = current.next
    return head


if __name__ == '__main__':
    ll = [5, 7, 5, 5, 7, 8, 4, 1]
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
    
    



