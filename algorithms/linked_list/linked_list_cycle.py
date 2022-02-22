class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def has_cycle(head):
    try:
        if head == None:
            return False
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
    except:
        return False

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

    head = has_cycle(head)

    # Print answer
    while head is not None:
        print(head.data)
        head = head.next
    
    



