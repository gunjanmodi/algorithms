class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Solution:
    def add_two_lists(self,first, second):
        
        node1 = self.reverse_linked_list(first)
        node2 = self.reverse_linked_list(second)
        new_head = Node(0)
        node = new_head
        total = 0
        while node1 or node2:
            total = total // 10
            if node1:
                total += node1.data
                node1 = node1.next
                
            if node2:
                total += node2.data
                node2 = node2.next
            
            node.next = Node(total % 10)
            node = node.next
        
        if total // 10 == 1:
            node.next = Node(1)
        
        return self.reverse_linked_list(new_head.next)
            
    def reverse_linked_list(self, head):
        previous, current = None, head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous

if __name__ == '__main__':
    ll = [4, 5]
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
