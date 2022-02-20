def remove_loop(self, head):
    fast = slow = head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        
        if slow == fast:
            break
    
    slow = head
    while slow and fast and slow != fast:
        slow = slow.next
        fast = fast.next
        
    if fast is None:
        return
        
    while fast.next != slow:
        fast = fast.next
        
    fast.next = None