class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Solution:
    def addOne(self,head):
        
        tail = self.reverse_linked_list(head)
        
        node = tail
        node.data += 1
        
        while node and node.data > 9:
            node.data = 0
            if node.next:
                node.next.data += 1
            else:
                node.next = Node(1)
            node = node.next
        
        return self.reverse_linked_list(tail)
            
    def reverse_linked_list(self, head):
        previous, current = None, head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous

if __name__ == '__main__':
    ll = [1, 2, 3, 4, 5]
    i = 1
    head = Node(ll[0])
    head_copy = head
    while i < len(ll):
        next_node = Node(ll[i])
        head.next = next_node
        head = next_node
        i += 1

    head = head_copy
    s = Solution()
    head = s.addOne(head)

    # Print answer
    while head is not None:
        print(head.data)
        head = head.next
