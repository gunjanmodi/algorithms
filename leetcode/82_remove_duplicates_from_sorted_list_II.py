from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:    
        node = head
        duplicated = set()
        while node and node.next:
            if node.val == node.next.val:
                duplicated.add(node.val)
            node = node.next
            
        node = head
        prev = ListNode(float('-inf'))
        while node:
            if node.val in duplicated:
                prev.next = node.next
                if node == head:
                    head = head.next
            else:
                prev = node
            node = node.next 
        return head