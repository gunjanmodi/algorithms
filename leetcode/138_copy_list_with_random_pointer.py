from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        d = {}
        node = head
        while node:
            if node not in d:
                d[node] = Node(node.val)
            if node.next and node.next not in d:
                d[node.next] = Node(node.next.val)
            if node.random and node.random not in d:
                d[node.random] = Node(node.random.val)
            
            if node.next:
                d[node].next = d.get(node.next)
            if node.random:
                d[node].random = d.get(node.random)
            else:
                d[node].random = None
                
            node = node.next
        return d[head]