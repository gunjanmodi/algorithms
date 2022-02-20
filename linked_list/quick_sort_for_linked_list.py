from sorting.quick_sort import quick_sort_helper


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

def quick_sort(head):
    ll_length, tail = get_len_linked_list(head)
    quick_sort_helper(head, tail)

def quick_sort_helper(head, tail):

    pivot = tail
    left = head
    right = tail

    while head != tail:
        if head.data < tail:
            



def get_len_linked_list(head):
    count = 0
    prev = None
    while head:
        count += 1
        prev = head
        head = head.next
    return count, prev


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

    head = quick_sort(head)

    # Print answer
    while head is not None:
        print(head.data)
        head = head.next
    
    



