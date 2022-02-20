class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

def merge_sort(head):
    if not head:
        return
    list_length = get_len_linked_list(head)
    return merge_sort_helper(head, list_length)


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

    head = merge_sort(head)

    # Print answer
    while head is not None:
        print(head.data)
        head = head.next
    
    



