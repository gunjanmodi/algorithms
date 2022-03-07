class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = node = ListNode(val=-1001)
        node1 = list1
        node2 = list2
        while node1 is not None and node2 is not None:
            if node1.val <= node2.val:
                node.next = node1
                node1 = node1.next
            else:
                node.next = node2
                node2 = node2.next
            node = node.next
        
        while node1 is not None:
            node.next = node1
            node1 = node1.next
            node = node.next
            
        while node2 is not None:
            node.next = node2
            node2 = node2.next
            node = node.next
            
        return head.next