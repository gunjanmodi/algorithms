import unittest

def rearrange_linked_list(head, k):
    smaller_list_head = None
    smaller_list_tail = None
    equal_list_head = None
    equal_list_tail = None
    greater_list_head = None
    greater_list_tail = None

    node = head
    while node is not None:
        if node.value < k:
            smaller_list_head,  smaller_list_tail = grow_linked_list(smaller_list_head, smaller_list_tail, node)
        elif node.value > k:
            greater_list_head,  greater_list_tail = grow_linked_list(greater_list_head, greater_list_tail, node)
        else:
            equal_list_head,  equal_list_tail = grow_linked_list(equal_list_head, equal_list_tail, node)
        
        prev_node = node
        node = node.next
        prev_node.next = None

    first_head, first_tail = connect_linked_list(smaller_list_head,  smaller_list_tail, equal_list_head,  equal_list_tail)
    final_head, _ = connect_linked_list(first_head,  first_tail, greater_list_head,  greater_list_tail)
    return final_head

def connect_linked_list(head_one, tail_one, head_two, tail_two):
    new_head = head_two if head_one is None else head_one
    new_tail = tail_one if tail_two is None else tail_two

    if tail_one is not None:
        tail_one.next = head_two

    return (new_head, new_tail)

def grow_linked_list(head, tail, node):
    new_head = head
    new_tail = node

    if new_head is None:
        new_head = node
    if tail is not None:
        tail.next = node
    return (new_head, new_tail)

def linked_list_to_array(head):
    array = []
    current = head
    while current is not None:
        array.append(current.value)
        current = current.next
    return array


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        head = LinkedList(3)
        head.next = LinkedList(0)
        head.next.next = LinkedList(5)
        head.next.next.next = LinkedList(2)
        head.next.next.next.next = LinkedList(1)
        head.next.next.next.next.next = LinkedList(4)
        result = rearrange_linked_list(head, 3)
        array = linked_list_to_array(result)

        expected = [0, 2, 1, 3, 5, 4]
        self.assertEqual(expected, array)


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


if __name__ == '__main__':
    unittest.main()
