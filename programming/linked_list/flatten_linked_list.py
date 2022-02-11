class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.bottom = None


def flatten(head):    
    head = flatten_helper(head)
    list_length = get_len_linked_list(head)
    head = merge_sort_helper(head, list_length)
    return head
    

def flatten_helper(head):
    if head is None:
        return head
    node = head
    next_node = node.next
    while node and node.bottom:
        node.next = node.bottom
        node = node.bottom
    node.next = next_node
    node = node.next
    flatten_helper(node)
    return head

def merge_sort_helper(head, list_length):
    if list_length == 1:
        return head

    mid = list_length // 2

    node1 = node2 = head
    prev = None
    count = 0
    while count < mid:
        prev = node2
        node2 = node2.next
        count += 1

    prev.next = None

    half1 = merge_sort_helper(node1, mid)
    half2 = merge_sort_helper(node2, list_length - mid)
    return merge(half1, half2, mid, list_length - mid)

def merge(half1, half2, len1, len2):
    sorted_head = Node(-1)
    node = sorted_head
    i, j = 0, 0

    while half1 and half2 and i < len1 and j < len2:
        if half1.data < half2.data:
            node.next = half1
            half1 = half1.next
            i += 1
        else:
            node.next = half2
            half2 = half2.next
            j += 1
        node = node.next

    while half1 and i < len1:
        node.next = half1
        half1 = half1.next
        node = node.next
        i += 1
    
    while half2 and j < len2:
        node.next = half2
        half2 = half2.next
        node = node.next
        j += 1

    return sorted_head.next

def get_len_linked_list(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count


if __name__ == '__main__':
    node5 = Node(5)
    node7 = Node(7)
    node8 = Node(8)
    node30 = Node(30)
    node5.bottom = node7
    node7.bottom = node8
    node8.bottom = node30

    node10 = Node(10)
    node20 = Node(20)
    node10.bottom = node20

    node19 = Node(19)
    node22 = Node(22)
    node50 = Node(50)
    node19.bottom = node22
    node22.bottom = node50

    node28 = Node(28)
    node35 = Node(35)
    node40 = Node(40)
    node45 = Node(45)
    node28.bottom = node35
    node35.bottom = node40
    node40.bottom = node45

    node5.next = node10
    node10.next = node19
    node19.next = node28

    head = node5

    head = flatten(head)

    # Print answer
    while head is not None:
        print(head.data)
        head = head.next