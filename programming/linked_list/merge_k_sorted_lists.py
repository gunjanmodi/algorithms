from heapq import heappop, heappush


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def merge_k_sorted_lists(lists):
    if len(lists) == 1:
        return lists[0]

    new_head = new_node = Node(0)

    min_heap = []
    for i, head in enumerate(lists):
        if head:
            heappush(min_heap, (head.data, i))

    while min_heap:
        value, min_index = heappop(min_heap)
        new_node.next = Node(value)
        new_node = new_node.next
        if lists[min_index].next:
            lists[min_index] = lists[min_index].next
            heappush(min_heap, (lists[min_index].data, min_index))

    return new_head.next


if __name__ == '__main__':
    l1 = Node(1)
    l1.next = Node(4)
    l1.next.next = Node(5)

    l2 = Node(1)
    l2.next = Node(3)
    l2.next.next = Node(4)

    l3 = Node(2)
    l3.next = Node(6)

    array = [l1, l2, l3]
    head = merge_k_sorted_lists(array)

    # Print answer
    while head is not None:
        print(head.data)
        head = head.next