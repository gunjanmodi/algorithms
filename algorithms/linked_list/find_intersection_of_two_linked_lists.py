class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def getIntersectionNode(head_a, head_b):
    len_a = len_ll(head_a)
    len_b = len_ll(head_b)
    
    node_a, node_b = head_a, head_b
    
    if len_a > len_b:
        while node_a and len_a != len_b:
            node_a = node_a.next
            len_a -= 1
                    
    elif len_a < len_b:
        while node_b and len_a != len_b:
            node_b = node_b.next
            len_b -= 1
            
    while node_a and node_b and node_a != node_b:
        node_a = node_a.next
        node_b = node_b.next
    else:
        return node_a.data
        

def len_ll(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next      
    return count