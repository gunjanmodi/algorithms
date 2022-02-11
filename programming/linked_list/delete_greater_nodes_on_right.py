class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

def compute(head):
    node = head
    stack = []
    while node:
        if len(stack) == 0:
            stack.append(node)
        elif len(stack) > 0 and stack[-1].data > node.data:
            stack.append(node)
        elif len(stack) > 0 and stack[-1].data < node.data:
            while stack and stack[-1].data < node.data:
                stack.pop()
            stack.append(node)    
        node = node.next

    stack.reverse()

    new_head = head
    if len(stack) > 0:
        new_head = new_node = stack.pop()
        while stack:
            new_node.next = stack.pop()
            new_node = new_node.next
    return new_head


def compute_2(head):
    node = head
    while node and node.next:
        if node.next.data > node.data:
            node.data = node.next.data
            node.next = node.next.next
        else:
            node = node.next
    return head


if __name__ == '__main__':
    ll = [12, 15,  10, 11 , 5, 6, 2, 3]
    i = 1
    head = Node(ll[0])
    head_copy = head
    while i < len(ll):
        next_node = Node(ll[i])
        head.next = next_node
        head = next_node
        i += 1

    head = head_copy

    head = compute(head)

    # Print answer
    while head is not None:
        print(head.data)
        head = head.next
    
    



