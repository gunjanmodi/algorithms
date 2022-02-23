"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
"""


from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node': # noqa
        if not node:
            return node

        # In the first pass, we will create the nodes
        d = {}
        q = deque()
        q.append(node)
        while q:
            current = q.popleft()
            new_node = d.get(current.val)
            if not new_node:
                new_node = Node(val=current.val)

            d[new_node.val] = new_node
            for child in current.neighbors:
                if child.val not in d:
                    q.append(child)

        # In the second pass, we will assign neighbors.
        q.append(node)
        visited = set()
        while q:
            current = q.popleft()
            if current.val in visited:
                continue
            visited.add(current.val)
            for child in current.neighbors:
                d[current.val].neighbors.append(d[child.val])
                if child.val not in visited:
                    q.append(child)

        return d[node.val]


# Optimized solution in a single loop
class Solution2:
    def cloneGraph(self, node: 'Node') -> 'Node': # noqa
        if not node:
            return node
        d = {}
        q = deque()
        new_node = Node(val=node.val)
        d[node] = new_node
        q.append(node)

        while q:
            current = q.popleft()
            for child in current.neighbors:
                if child not in d:
                    q.append(child)
                    d[child] = Node(val=child.val)
                d[current].neighbors.append(d[child])
        return d[node]
