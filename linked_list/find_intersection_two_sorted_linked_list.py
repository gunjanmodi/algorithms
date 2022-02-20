class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def find_intersection(head1,head2):

    node1, node2 = head1, head2
    new_node = Node(0)
    node = new_node
    
    while node1 and node2:
        if node1.data == node2.data:
            node.next = Node(node1.data)
            node1 = node1.next
            node2 = node2.next
            node = node.next
            
        elif node1.data < node2.data:
            node1 = node1.next
            
        else:
            node2 = node2.next
            
    return new_node.next


def find_intersection(head1,head2):
    visited1, visited2 = set(), set()
    node1, node2 = head1, head2
    while node1:
        visited1.add(node1.data)
        node1 = node1.next
    
    new_node = Node(0)
    node = new_node
    while node2 and node:
        if node2.data in visited1 and node2.data not in visited2:
            node.next = Node(node2.data)
            visited2.add(node2.data)
            node = node.next
        node2 = node2.next
        
    return new_node.next