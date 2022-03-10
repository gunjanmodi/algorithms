from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = new_node = ListNode(-1)
        p1, p2 = l1, l2
        carry = 0
        while p1 or p2:
            total = carry
            if p1:
                total += p1.val
            if p2:
                total += p2.val
            if total <= 9:
                new_node.next = ListNode(total)
                carry = 0
            else:
                new_node.next = ListNode(total % 10)
                carry = total // 10
            new_node = new_node.next   
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        
        if carry > 0:
            new_node.next = ListNode(carry)
        return new_head.next